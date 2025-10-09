from rest_framework import generics, status, permissions, filters
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Q, Sum, Count, Avg
from django.db import models
from django.utils import timezone
from datetime import datetime, timedelta
from .models import Appointment, AppointmentReminder, AppointmentFeedback, AppointmentDocument, AppointmentPayment
from .serializers import (
    AppointmentSerializer, AppointmentListSerializer, AppointmentCreateSerializer,
    AppointmentUpdateSerializer, AppointmentReminderSerializer, AppointmentFeedbackSerializer,
    AppointmentDocumentSerializer, AppointmentPaymentSerializer, AppointmentStatsSerializer
)


class AppointmentListView(generics.ListAPIView):
    """List appointments with filtering."""
    
    serializer_class = AppointmentListSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['status', 'urgency', 'doctor', 'service', 'appointment_date', 'payment_status']
    search_fields = ['symptoms', 'notes', 'doctor__name', 'service__name']
    ordering_fields = ['appointment_date', 'appointment_time', 'created_at', 'total_cost']
    ordering = ['-appointment_date', '-appointment_time']
    
    def get_queryset(self):
        user = self.request.user
        if user.user_type in ['admin', 'staff']:
            return Appointment.objects.all()
        elif user.user_type == 'doctor':
            return Appointment.objects.filter(doctor__user=user)
        else:  # patient
            return Appointment.objects.filter(patient=user)


class AppointmentDetailView(generics.RetrieveAPIView):
    """Get appointment details."""
    
    serializer_class = AppointmentSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        if user.user_type in ['admin', 'staff']:
            return Appointment.objects.all()
        elif user.user_type == 'doctor':
            return Appointment.objects.filter(doctor__user=user)
        else:  # patient
            return Appointment.objects.filter(patient=user)


class AppointmentCreateView(generics.CreateAPIView):
    """Create a new appointment."""
    
    serializer_class = AppointmentCreateSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def perform_create(self, serializer):
        # Only patients can create appointments
        if self.request.user.user_type != 'patient':
            raise permissions.PermissionDenied("Only patients can create appointments")
        serializer.save(patient=self.request.user)


class AppointmentUpdateView(generics.UpdateAPIView):
    """Update appointment."""
    
    serializer_class = AppointmentUpdateSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        if user.user_type in ['admin', 'staff']:
            return Appointment.objects.all()
        elif user.user_type == 'doctor':
            return Appointment.objects.filter(doctor__user=user)
        else:  # patient
            return Appointment.objects.filter(patient=user)


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def cancel_appointment(request, appointment_id):
    """Cancel an appointment."""
    try:
        appointment = Appointment.objects.get(id=appointment_id)
    except Appointment.DoesNotExist:
        return Response({'error': 'Appointment not found'}, status=status.HTTP_404_NOT_FOUND)
    
    # Check permissions
    user = request.user
    if user.user_type not in ['admin', 'staff'] and appointment.patient != user:
        return Response({'error': 'Permission denied'}, status=status.HTTP_403_FORBIDDEN)
    
    if not appointment.can_be_cancelled:
        return Response({'error': 'Appointment cannot be cancelled'}, status=status.HTTP_400_BAD_REQUEST)
    
    appointment.status = 'cancelled'
    appointment.cancelled_at = timezone.now()
    appointment.save()
    
    return Response({'message': 'Appointment cancelled successfully'})


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def confirm_appointment(request, appointment_id):
    """Confirm an appointment."""
    try:
        appointment = Appointment.objects.get(id=appointment_id)
    except Appointment.DoesNotExist:
        return Response({'error': 'Appointment not found'}, status=status.HTTP_404_NOT_FOUND)
    
    # Check permissions
    user = request.user
    if user.user_type not in ['admin', 'staff', 'doctor']:
        return Response({'error': 'Permission denied'}, status=status.HTTP_403_FORBIDDEN)
    
    if appointment.status != 'pending':
        return Response({'error': 'Only pending appointments can be confirmed'}, status=status.HTTP_400_BAD_REQUEST)
    
    appointment.status = 'confirmed'
    appointment.confirmed_at = timezone.now()
    appointment.save()
    
    return Response({'message': 'Appointment confirmed successfully'})


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def available_slots(request, doctor_id, date):
    """Get available time slots for a doctor on a specific date."""
    try:
        from apps.doctors.models import Doctor
        doctor = Doctor.objects.get(id=doctor_id)
    except Doctor.DoesNotExist:
        return Response({'error': 'Doctor not found'}, status=status.HTTP_404_NOT_FOUND)
    
    # Parse date
    try:
        appointment_date = datetime.strptime(date, '%Y-%m-%d').date()
    except ValueError:
        return Response({'error': 'Invalid date format. Use YYYY-MM-DD'}, status=status.HTTP_400_BAD_REQUEST)
    
    # Get doctor's schedule for the day
    from apps.doctors.models import DoctorSchedule
    day_of_week = appointment_date.strftime('%A').lower()
    try:
        schedule = DoctorSchedule.objects.get(doctor=doctor, day_of_week=day_of_week)
    except DoctorSchedule.DoesNotExist:
        return Response({'error': 'Doctor not available on this day'}, status=status.HTTP_400_BAD_REQUEST)
    
    # Generate available time slots
    available_slots = []
    current_time = datetime.combine(appointment_date, schedule.start_time)
    end_time = datetime.combine(appointment_date, schedule.end_time)
    
    while current_time < end_time:
        # Check if slot is available
        existing_appointment = Appointment.objects.filter(
            doctor=doctor,
            appointment_date=appointment_date,
            appointment_time=current_time.time(),
            status__in=['pending', 'confirmed']
        ).exists()
        
        if not existing_appointment:
            available_slots.append(current_time.strftime('%H:%M'))
        
        current_time += timedelta(minutes=30)  # 30-minute slots
    
    return Response({
        'doctor': doctor.name,
        'date': date,
        'available_slots': available_slots,
        'schedule': {
            'start_time': schedule.start_time.strftime('%H:%M'),
            'end_time': schedule.end_time.strftime('%H:%M'),
            'max_appointments': schedule.max_appointments
        }
    })


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def appointment_stats(request):
    """Get appointment statistics."""
    user = request.user
    
    # Base queryset based on user type
    if user.user_type in ['admin', 'staff']:
        appointments = Appointment.objects.all()
    elif user.user_type == 'doctor':
        appointments = Appointment.objects.filter(doctor__user=user)
    else:  # patient
        appointments = Appointment.objects.filter(patient=user)
    
    # Calculate statistics
    total_appointments = appointments.count()
    pending_appointments = appointments.filter(status='pending').count()
    confirmed_appointments = appointments.filter(status='confirmed').count()
    completed_appointments = appointments.filter(status='completed').count()
    cancelled_appointments = appointments.filter(status='cancelled').count()
    
    # Calculate revenue
    total_revenue = appointments.filter(
        status='completed',
        payment_status='paid'
    ).aggregate(total=Sum('total_cost'))['total'] or 0
    
    # Calculate average rating
    average_rating = appointments.filter(
        status='completed',
        feedback__isnull=False
    ).aggregate(avg_rating=Avg('feedback__overall_rating'))['avg_rating'] or 0
    
    # Today's appointments
    today = timezone.now().date()
    today_appointments = appointments.filter(appointment_date=today).count()
    
    # Upcoming appointments
    upcoming_appointments = appointments.filter(
        appointment_date__gte=today,
        status__in=['pending', 'confirmed']
    ).count()
    
    stats = {
        'total_appointments': total_appointments,
        'pending_appointments': pending_appointments,
        'confirmed_appointments': confirmed_appointments,
        'completed_appointments': completed_appointments,
        'cancelled_appointments': cancelled_appointments,
        'total_revenue': total_revenue,
        'average_rating': average_rating,
        'today_appointments': today_appointments,
        'upcoming_appointments': upcoming_appointments
    }
    
    serializer = AppointmentStatsSerializer(stats)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def add_feedback(request, appointment_id):
    """Add feedback for an appointment."""
    try:
        appointment = Appointment.objects.get(id=appointment_id)
    except Appointment.DoesNotExist:
        return Response({'error': 'Appointment not found'}, status=status.HTTP_404_NOT_FOUND)
    
    # Check permissions
    if appointment.patient != request.user:
        return Response({'error': 'Permission denied'}, status=status.HTTP_403_FORBIDDEN)
    
    # Check if appointment is completed
    if appointment.status != 'completed':
        return Response({'error': 'Feedback can only be added for completed appointments'}, status=status.HTTP_400_BAD_REQUEST)
    
    # Create or update feedback
    feedback, created = AppointmentFeedback.objects.get_or_create(
        appointment=appointment,
        defaults=request.data
    )
    
    if not created:
        serializer = AppointmentFeedbackSerializer(feedback, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # Update doctor's rating
    appointment.doctor.update_rating()
    
    return Response({'message': 'Feedback added successfully'})


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def upload_document(request, appointment_id):
    """Upload document for an appointment."""
    try:
        appointment = Appointment.objects.get(id=appointment_id)
    except Appointment.DoesNotExist:
        return Response({'error': 'Appointment not found'}, status=status.HTTP_404_NOT_FOUND)
    
    # Check permissions
    user = request.user
    if user.user_type not in ['admin', 'staff', 'doctor'] and appointment.patient != user:
        return Response({'error': 'Permission denied'}, status=status.HTTP_403_FORBIDDEN)
    
    # Add uploaded_by to request data
    request.data['uploaded_by'] = user.id
    request.data['appointment'] = appointment_id
    
    serializer = AppointmentDocumentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)