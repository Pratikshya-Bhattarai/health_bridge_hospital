from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Patient(models.Model):
    """Patient model extending user information."""
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='patient_profile')
    
    # Medical Information
    blood_type = models.CharField(max_length=5, blank=True, choices=[
        ('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'),
        ('AB+', 'AB+'), ('AB-', 'AB-'), ('O+', 'O+'), ('O-', 'O-'),
    ])
    allergies = models.TextField(blank=True)
    medical_conditions = models.TextField(blank=True)
    current_medications = models.TextField(blank=True)
    
    # Emergency Contact
    emergency_contact_name = models.CharField(max_length=100, blank=True)
    emergency_contact_phone = models.CharField(max_length=17, blank=True)
    emergency_contact_relation = models.CharField(max_length=50, blank=True)
    
    # Insurance Information
    insurance_provider = models.CharField(max_length=100, blank=True)
    insurance_number = models.CharField(max_length=50, blank=True)
    insurance_expiry = models.DateField(null=True, blank=True)
    
    # Preferences
    preferred_language = models.CharField(max_length=10, default='en', choices=[
        ('en', 'English'),
        ('ne', 'Nepali'),
        ('hi', 'Hindi'),
    ])
    notification_preferences = models.JSONField(default=dict, blank=True)
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'patients'
        verbose_name = 'Patient'
        verbose_name_plural = 'Patients'
    
    def __str__(self):
        return f"{self.user.get_full_name()} - Patient"


class MedicalRecord(models.Model):
    """Medical record model."""
    
    RECORD_TYPE_CHOICES = [
        ('diagnosis', 'Diagnosis'),
        ('prescription', 'Prescription'),
        ('lab_result', 'Lab Result'),
        ('imaging', 'Imaging'),
        ('vaccination', 'Vaccination'),
        ('surgery', 'Surgery'),
        ('other', 'Other'),
    ]
    
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='medical_records')
    record_type = models.CharField(max_length=20, choices=RECORD_TYPE_CHOICES)
    title = models.CharField(max_length=200)
    description = models.TextField()
    diagnosis = models.TextField(blank=True)
    treatment = models.TextField(blank=True)
    medications = models.TextField(blank=True)
    notes = models.TextField(blank=True)
    
    # File attachments
    attachments = models.JSONField(default=list, blank=True)  # Store file paths
    
    # Doctor information
    doctor_name = models.CharField(max_length=100)
    doctor_license = models.CharField(max_length=50, blank=True)
    
    # Timestamps
    record_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'medical_records'
        verbose_name = 'Medical Record'
        verbose_name_plural = 'Medical Records'
        ordering = ['-record_date']
    
    def __str__(self):
        return f"{self.patient.user.get_full_name()} - {self.title}"