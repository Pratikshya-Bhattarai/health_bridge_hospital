from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone
from apps.doctors.models import Doctor
from apps.services.models import Service

User = get_user_model()


class Appointment(models.Model):
    """Appointment model for booking system."""
    
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
        ('no_show', 'No Show'),
        ('rescheduled', 'Rescheduled'),
    ]
    
    URGENCY_CHOICES = [
        ('routine', 'Routine'),
        ('urgent', 'Urgent'),
        ('emergency', 'Emergency'),
    ]
    
    PAYMENT_STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('paid', 'Paid'),
        ('partial', 'Partial'),
        ('refunded', 'Refunded'),
    ]
    
    # Basic Information
    patient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='appointments')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='appointments')
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='appointments')
    
    # Appointment Details
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    duration_minutes = models.IntegerField(default=30, validators=[MinValueValidator(15), MaxValueValidator(240)])
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    urgency = models.CharField(max_length=10, choices=URGENCY_CHOICES, default='routine')
    
    # Medical Information
    symptoms = models.TextField(blank=True)
    medical_history = models.TextField(blank=True)
    current_medications = models.TextField(blank=True)
    allergies = models.TextField(blank=True)
    vital_signs = models.JSONField(default=dict, blank=True)  # Store BP, temperature, etc.
    
    # Additional Information
    notes = models.TextField(blank=True)
    special_requirements = models.TextField(blank=True)
    follow_up_required = models.BooleanField(default=False)
    follow_up_date = models.DateField(null=True, blank=True)
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    confirmed_at = models.DateTimeField(null=True, blank=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    cancelled_at = models.DateTimeField(null=True, blank=True)
    
    # Cost Information
    consultation_fee = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    additional_charges = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    discount_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    payment_status = models.CharField(max_length=10, choices=PAYMENT_STATUS_CHOICES, default='pending')
    
    # External References
    external_id = models.CharField(max_length=100, blank=True)  # For integration with external systems
    referral_source = models.CharField(max_length=100, blank=True)
    
    class Meta:
        ordering = ['-appointment_date', '-appointment_time']
        unique_together = ['doctor', 'appointment_date', 'appointment_time']
        db_table = 'appointments'
        verbose_name = 'Appointment'
        verbose_name_plural = 'Appointments'
    
    def __str__(self):
        return f"{self.patient.get_full_name()} - {self.doctor.name} - {self.appointment_date} {self.appointment_time}"
    
    def save(self, *args, **kwargs):
        # Calculate total cost
        self.total_cost = self.consultation_fee + self.additional_charges - self.discount_amount
        super().save(*args, **kwargs)
    
    @property
    def is_past(self):
        """Check if appointment is in the past."""
        appointment_datetime = timezone.datetime.combine(self.appointment_date, self.appointment_time)
        return appointment_datetime < timezone.now()
    
    @property
    def is_today(self):
        """Check if appointment is today."""
        return self.appointment_date == timezone.now().date()
    
    @property
    def can_be_cancelled(self):
        """Check if appointment can be cancelled."""
        return self.status in ['pending', 'confirmed'] and not self.is_past


class AppointmentReminder(models.Model):
    """Appointment reminder model."""
    
    REMINDER_TYPE_CHOICES = [
        ('email', 'Email'),
        ('sms', 'SMS'),
        ('call', 'Phone Call'),
        ('push', 'Push Notification'),
    ]
    
    REMINDER_TIMING_CHOICES = [
        (15, '15 minutes before'),
        (30, '30 minutes before'),
        (60, '1 hour before'),
        (1440, '1 day before'),
        (2880, '2 days before'),
        (10080, '1 week before'),
    ]
    
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE, related_name='reminders')
    reminder_type = models.CharField(max_length=10, choices=REMINDER_TYPE_CHOICES)
    reminder_timing = models.IntegerField(choices=REMINDER_TIMING_CHOICES)
    reminder_datetime = models.DateTimeField()
    sent = models.BooleanField(default=False)
    sent_at = models.DateTimeField(null=True, blank=True)
    delivery_status = models.CharField(max_length=20, default='pending')
    error_message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'appointment_reminders'
        verbose_name = 'Appointment Reminder'
        verbose_name_plural = 'Appointment Reminders'
    
    def __str__(self):
        return f"{self.appointment} - {self.get_reminder_type_display()} - {self.reminder_datetime}"


class AppointmentFeedback(models.Model):
    """Appointment feedback model."""
    
    RATING_CHOICES = [
        (1, 'Very Poor'),
        (2, 'Poor'),
        (3, 'Average'),
        (4, 'Good'),
        (5, 'Excellent'),
    ]
    
    appointment = models.OneToOneField(Appointment, on_delete=models.CASCADE, related_name='feedback')
    overall_rating = models.IntegerField(choices=RATING_CHOICES)
    doctor_rating = models.IntegerField(choices=RATING_CHOICES)
    service_rating = models.IntegerField(choices=RATING_CHOICES)
    facility_rating = models.IntegerField(choices=RATING_CHOICES)
    
    # Detailed feedback
    comment = models.TextField(blank=True)
    would_recommend = models.BooleanField(default=True)
    wait_time_satisfactory = models.BooleanField(default=True)
    staff_friendly = models.BooleanField(default=True)
    clean_facility = models.BooleanField(default=True)
    
    # Improvement suggestions
    improvement_suggestions = models.TextField(blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'appointment_feedback'
        verbose_name = 'Appointment Feedback'
        verbose_name_plural = 'Appointment Feedback'
    
    def __str__(self):
        return f"{self.appointment} - {self.overall_rating}/5"


class AppointmentDocument(models.Model):
    """Appointment document model."""
    
    DOCUMENT_TYPE_CHOICES = [
        ('prescription', 'Prescription'),
        ('lab_report', 'Lab Report'),
        ('xray', 'X-Ray'),
        ('mri', 'MRI'),
        ('ct_scan', 'CT Scan'),
        ('ultrasound', 'Ultrasound'),
        ('other', 'Other'),
    ]
    
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE, related_name='documents')
    document_type = models.CharField(max_length=20, choices=DOCUMENT_TYPE_CHOICES)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    file = models.FileField(upload_to='appointment_documents/')
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='uploaded_documents')
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'appointment_documents'
        verbose_name = 'Appointment Document'
        verbose_name_plural = 'Appointment Documents'
    
    def __str__(self):
        return f"{self.appointment} - {self.title}"


class AppointmentPayment(models.Model):
    """Appointment payment model."""
    
    PAYMENT_METHOD_CHOICES = [
        ('cash', 'Cash'),
        ('card', 'Card'),
        ('bank_transfer', 'Bank Transfer'),
        ('mobile_payment', 'Mobile Payment'),
        ('insurance', 'Insurance'),
    ]
    
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE, related_name='payments')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES)
    transaction_id = models.CharField(max_length=100, blank=True)
    payment_date = models.DateTimeField(auto_now_add=True)
    processed_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='processed_payments')
    notes = models.TextField(blank=True)
    
    class Meta:
        db_table = 'appointment_payments'
        verbose_name = 'Appointment Payment'
        verbose_name_plural = 'Appointment Payments'
    
    def __str__(self):
        return f"{self.appointment} - {self.amount} - {self.payment_method}"