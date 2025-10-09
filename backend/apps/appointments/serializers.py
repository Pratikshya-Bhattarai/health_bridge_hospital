from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Appointment, AppointmentReminder, AppointmentFeedback, AppointmentDocument, AppointmentPayment
from apps.doctors.models import Doctor
from apps.services.models import Service

User = get_user_model()


class AppointmentSerializer(serializers.ModelSerializer):
    """Serializer for appointments."""
    
    patient_name = serializers.CharField(source='patient.get_full_name', read_only=True)
    doctor_name = serializers.CharField(source='doctor.name', read_only=True)
    service_name = serializers.CharField(source='service.name', read_only=True)
    
    class Meta:
        model = Appointment
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at', 'total_cost')
    
    def create(self, validated_data):
        # Set consultation fee from doctor's fee
        doctor = validated_data['doctor']
        validated_data['consultation_fee'] = doctor.consultation_fee
        return super().create(validated_data)


class AppointmentListSerializer(serializers.ModelSerializer):
    """Serializer for listing appointments."""
    
    patient_name = serializers.CharField(source='patient.get_full_name', read_only=True)
    doctor_name = serializers.CharField(source='doctor.name', read_only=True)
    service_name = serializers.CharField(source='service.name', read_only=True)
    status_display = serializers.CharField(source='get_status_display', read_only=True)
    urgency_display = serializers.CharField(source='get_urgency_display', read_only=True)
    
    class Meta:
        model = Appointment
        fields = (
            'id', 'patient', 'patient_name', 'doctor', 'doctor_name',
            'service', 'service_name', 'appointment_date', 'appointment_time',
            'status', 'status_display', 'urgency', 'urgency_display',
            'consultation_fee', 'total_cost', 'payment_status',
            'created_at', 'updated_at'
        )


class AppointmentCreateSerializer(serializers.ModelSerializer):
    """Serializer for creating appointments."""
    
    class Meta:
        model = Appointment
        fields = (
            'doctor', 'service', 'appointment_date', 'appointment_time',
            'symptoms', 'medical_history', 'current_medications', 'allergies',
            'urgency', 'notes', 'special_requirements', 'follow_up_required'
        )
    
    def validate(self, data):
        # Check if doctor is available
        doctor = data['doctor']
        if not doctor.is_available:
            raise serializers.ValidationError("Doctor is not available")
        
        # Check if appointment time is in the future
        from django.utils import timezone
        appointment_datetime = timezone.datetime.combine(
            data['appointment_date'], data['appointment_time']
        )
        if appointment_datetime <= timezone.now():
            raise serializers.ValidationError("Appointment time must be in the future")
        
        # Check for conflicting appointments
        existing_appointment = Appointment.objects.filter(
            doctor=data['doctor'],
            appointment_date=data['appointment_date'],
            appointment_time=data['appointment_time'],
            status__in=['pending', 'confirmed']
        ).exists()
        
        if existing_appointment:
            raise serializers.ValidationError("Time slot is already booked")
        
        return data


class AppointmentUpdateSerializer(serializers.ModelSerializer):
    """Serializer for updating appointments."""
    
    class Meta:
        model = Appointment
        fields = (
            'appointment_date', 'appointment_time', 'symptoms',
            'medical_history', 'current_medications', 'allergies',
            'urgency', 'notes', 'special_requirements', 'follow_up_required',
            'follow_up_date'
        )


class AppointmentReminderSerializer(serializers.ModelSerializer):
    """Serializer for appointment reminders."""
    
    class Meta:
        model = AppointmentReminder
        fields = '__all__'


class AppointmentFeedbackSerializer(serializers.ModelSerializer):
    """Serializer for appointment feedback."""
    
    class Meta:
        model = AppointmentFeedback
        fields = '__all__'


class AppointmentDocumentSerializer(serializers.ModelSerializer):
    """Serializer for appointment documents."""
    
    uploaded_by_name = serializers.CharField(source='uploaded_by.get_full_name', read_only=True)
    
    class Meta:
        model = AppointmentDocument
        fields = '__all__'
        read_only_fields = ('uploaded_by', 'created_at')


class AppointmentPaymentSerializer(serializers.ModelSerializer):
    """Serializer for appointment payments."""
    
    processed_by_name = serializers.CharField(source='processed_by.get_full_name', read_only=True)
    
    class Meta:
        model = AppointmentPayment
        fields = '__all__'
        read_only_fields = ('processed_by', 'payment_date')


class AppointmentStatsSerializer(serializers.Serializer):
    """Serializer for appointment statistics."""
    
    total_appointments = serializers.IntegerField()
    pending_appointments = serializers.IntegerField()
    confirmed_appointments = serializers.IntegerField()
    completed_appointments = serializers.IntegerField()
    cancelled_appointments = serializers.IntegerField()
    total_revenue = serializers.DecimalField(max_digits=10, decimal_places=2)
    average_rating = serializers.DecimalField(max_digits=3, decimal_places=2)
    today_appointments = serializers.IntegerField()
    upcoming_appointments = serializers.IntegerField()