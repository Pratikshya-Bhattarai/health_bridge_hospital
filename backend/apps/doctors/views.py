from rest_framework import generics, status, permissions, filters
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Q, Avg, Count, Sum
from django.db import models
from datetime import datetime, timedelta
from .models import Doctor, DoctorSchedule, DoctorSpecialization
from .serializers import (
    DoctorSerializer, DoctorListSerializer, DoctorDetailSerializer,
    DoctorCreateSerializer, DoctorUpdateSerializer, DoctorStatsSerializer,
    DoctorScheduleSerializer, DoctorSpecializationSerializer
)


class DoctorListView(generics.ListAPIView):
    """List all doctors with filtering and search."""
    
    serializer_class = DoctorListSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['specialty', 'is_available', 'experience_years']
    search_fields = ['name', 'specialty', 'qualification', 'bio']
    ordering_fields = ['name', 'experience_years', 'consultation_fee', 'average_rating']
    ordering = ['-average_rating', 'name']
    
    def get_queryset(self):
        return Doctor.objects.filter(is_available=True)


class DoctorDetailView(generics.RetrieveAPIView):
    """Get doctor details."""
    
    serializer_class = DoctorDetailSerializer
    permission_classes = [permissions.AllowAny]
    queryset = Doctor.objects.all()


class DoctorCreateView(generics.CreateAPIView):
    """Create a new doctor (admin/staff only)."""
    
    serializer_class = DoctorCreateSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def perform_create(self, serializer):
        if self.request.user.user_type not in ['admin', 'staff']:
            raise permissions.PermissionDenied("Only admin and staff can create doctors")
        serializer.save()


class DoctorUpdateView(generics.UpdateAPIView):
    """Update doctor information."""
    
    serializer_class = DoctorUpdateSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Doctor.objects.all()
    
    def get_object(self):
        doctor = super().get_object()
        # Only allow doctor to update their own profile or admin/staff to update any
        if (self.request.user.user_type not in ['admin', 'staff'] and 
            doctor.user != self.request.user):
            raise permissions.PermissionDenied("You can only update your own profile")
        return doctor


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def doctor_availability(request, doctor_id, date):
    """Get doctor's available time slots for a specific date."""
    try:
        doctor = Doctor.objects.get(id=doctor_id)
    except Doctor.DoesNotExist:
        return Response({'error': 'Doctor not found'}, status=status.HTTP_404_NOT_FOUND)
    
    # Parse date
    try:
        appointment_date = datetime.strptime(date, '%Y-%m-%d').date()
    except ValueError:
        return Response({'error': 'Invalid date format. Use YYYY-MM-DD'}, status=status.HTTP_400_BAD_REQUEST)
    
    # Get doctor's schedule for the day of week
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
        # Check if slot is available (not booked)
        from apps.appointments.models import Appointment
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
def doctor_stats(request, doctor_id):
    """Get doctor statistics."""
    try:
        doctor = Doctor.objects.get(id=doctor_id)
    except Doctor.DoesNotExist:
        return Response({'error': 'Doctor not found'}, status=status.HTTP_404_NOT_FOUND)
    
    # Only allow doctor to view their own stats or admin/staff to view any
    if (request.user.user_type not in ['admin', 'staff'] and 
        doctor.user != request.user):
        return Response({'error': 'Permission denied'}, status=status.HTTP_403_FORBIDDEN)
    
    from apps.appointments.models import Appointment
    
    # Get appointment statistics
    appointments = Appointment.objects.filter(doctor=doctor)
    total_appointments = appointments.count()
    completed_appointments = appointments.filter(status='completed').count()
    pending_appointments = appointments.filter(status='pending').count()
    cancelled_appointments = appointments.filter(status='cancelled').count()
    
    # Calculate revenue
    total_revenue = appointments.filter(
        status='completed',
        payment_status='paid'
    ).aggregate(
        total=models.Sum('total_cost')
    )['total'] or 0
    
    # Get next appointment
    next_appointment = appointments.filter(
        status__in=['pending', 'confirmed'],
        appointment_date__gte=datetime.now().date()
    ).order_by('appointment_date', 'appointment_time').first()
    
    stats = {
        'total_appointments': total_appointments,
        'completed_appointments': completed_appointments,
        'pending_appointments': pending_appointments,
        'cancelled_appointments': cancelled_appointments,
        'total_revenue': total_revenue,
        'average_rating': doctor.average_rating,
        'total_reviews': doctor.total_reviews,
        'next_appointment': next_appointment.created_at if next_appointment else None
    }
    
    serializer = DoctorStatsSerializer(stats)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def doctor_specialties(request):
    """Get list of available doctor specialties."""
    specialties = Doctor.SPECIALTY_CHOICES
    return Response([{'value': choice[0], 'label': choice[1]} for choice in specialties])


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def featured_doctors(request):
    """Get featured doctors (highest rated)."""
    doctors = Doctor.objects.filter(
        is_available=True,
        average_rating__gte=4.0
    ).order_by('-average_rating', '-total_reviews')[:6]
    
    serializer = DoctorListSerializer(doctors, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def search_doctors(request):
    """Search doctors by specialty, name, or location."""
    query = request.GET.get('q', '')
    specialty = request.GET.get('specialty', '')
    min_rating = request.GET.get('min_rating', 0)
    max_fee = request.GET.get('max_fee', None)
    
    queryset = Doctor.objects.filter(is_available=True)
    
    if query:
        queryset = queryset.filter(
            Q(name__icontains=query) |
            Q(specialty__icontains=query) |
            Q(qualification__icontains=query) |
            Q(bio__icontains=query)
        )
    
    if specialty:
        queryset = queryset.filter(specialty=specialty)
    
    if min_rating:
        queryset = queryset.filter(average_rating__gte=float(min_rating))
    
    if max_fee:
        queryset = queryset.filter(consultation_fee__lte=float(max_fee))
    
    serializer = DoctorListSerializer(queryset, many=True)
    return Response(serializer.data)