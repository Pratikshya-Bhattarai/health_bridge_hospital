from rest_framework import serializers
from .models import Patient, MedicalRecord


class PatientSerializer(serializers.ModelSerializer):
    """Serializer for patients."""
    
    user_name = serializers.CharField(source='user.get_full_name', read_only=True)
    user_email = serializers.CharField(source='user.email', read_only=True)
    user_phone = serializers.CharField(source='user.phone_number', read_only=True)
    
    class Meta:
        model = Patient
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')


class MedicalRecordSerializer(serializers.ModelSerializer):
    """Serializer for medical records."""
    
    patient_name = serializers.CharField(source='patient.user.get_full_name', read_only=True)
    
    class Meta:
        model = MedicalRecord
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')


class MedicalRecordCreateSerializer(serializers.ModelSerializer):
    """Serializer for creating medical records."""
    
    class Meta:
        model = MedicalRecord
        fields = (
            'record_type', 'title', 'description', 'diagnosis',
            'treatment', 'medications', 'notes', 'attachments',
            'doctor_name', 'doctor_license', 'record_date'
        )