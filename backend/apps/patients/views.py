from rest_framework import generics, status, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import Patient, MedicalRecord
from .serializers import PatientSerializer, MedicalRecordSerializer, MedicalRecordCreateSerializer


class PatientDetailView(generics.RetrieveUpdateAPIView):
    """Get and update patient profile."""
    
    serializer_class = PatientSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_object(self):
        patient, created = Patient.objects.get_or_create(user=self.request.user)
        return patient


class MedicalRecordListView(generics.ListCreateAPIView):
    """List and create medical records."""
    
    serializer_class = MedicalRecordSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        patient, created = Patient.objects.get_or_create(user=self.request.user)
        return MedicalRecord.objects.filter(patient=patient)


class MedicalRecordDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Get, update, and delete medical records."""
    
    serializer_class = MedicalRecordSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        patient, created = Patient.objects.get_or_create(user=self.request.user)
        return MedicalRecord.objects.filter(patient=patient)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def patient_dashboard(request):
    """Get patient dashboard data."""
    patient, created = Patient.objects.get_or_create(user=request.user)
    
    # Get recent appointments
    from apps.appointments.models import Appointment
    recent_appointments = Appointment.objects.filter(
        patient=request.user
    ).order_by('-appointment_date')[:5]
    
    # Get medical records count
    medical_records_count = MedicalRecord.objects.filter(patient=patient).count()
    
    # Get upcoming appointments
    from django.utils import timezone
    upcoming_appointments = Appointment.objects.filter(
        patient=request.user,
        appointment_date__gte=timezone.now().date(),
        status__in=['pending', 'confirmed']
    ).count()
    
    dashboard_data = {
        'patient': PatientSerializer(patient).data,
        'recent_appointments': [
            {
                'id': apt.id,
                'doctor_name': apt.doctor.name,
                'service_name': apt.service.name,
                'appointment_date': apt.appointment_date,
                'appointment_time': apt.appointment_time,
                'status': apt.status
            }
            for apt in recent_appointments
        ],
        'medical_records_count': medical_records_count,
        'upcoming_appointments': upcoming_appointments
    }
    
    return Response(dashboard_data)