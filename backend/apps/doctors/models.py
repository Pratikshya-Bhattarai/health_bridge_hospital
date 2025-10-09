from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator

User = get_user_model()


class Doctor(models.Model):
    """Doctor model."""
    
    SPECIALTY_CHOICES = [
        ('cardiology', 'Cardiology'),
        ('neurology', 'Neurology'),
        ('orthopedics', 'Orthopedics'),
        ('pediatrics', 'Pediatrics'),
        ('internal_medicine', 'Internal Medicine'),
        ('emergency_medicine', 'Emergency Medicine'),
        ('dermatology', 'Dermatology'),
        ('psychiatry', 'Psychiatry'),
        ('gynecology', 'Gynecology'),
        ('urology', 'Urology'),
        ('ophthalmology', 'Ophthalmology'),
        ('ent', 'ENT'),
        ('general_surgery', 'General Surgery'),
        ('anesthesiology', 'Anesthesiology'),
        ('radiology', 'Radiology'),
    ]
    
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]
    
    # Basic Information
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='doctor_profile')
    name = models.CharField(max_length=100)
    specialty = models.CharField(max_length=20, choices=SPECIALTY_CHOICES)
    qualification = models.CharField(max_length=200)
    experience_years = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(50)])
    consultation_fee = models.DecimalField(max_digits=10, decimal_places=2)
    
    # Professional Information
    license_number = models.CharField(max_length=50, unique=True)
    medical_council = models.CharField(max_length=100, default='Nepal Medical Council')
    bio = models.TextField(blank=True)
    education = models.TextField(blank=True)
    certifications = models.TextField(blank=True)
    
    # Contact Information
    phone_number = models.CharField(max_length=17, blank=True)
    email = models.EmailField(blank=True)
    address = models.TextField(blank=True)
    
    # Profile Information
    profile_image = models.ImageField(upload_to='doctors/', blank=True, null=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    
    # Availability
    is_available = models.BooleanField(default=True)
    working_hours = models.JSONField(default=dict, blank=True)  # Store working hours
    available_days = models.JSONField(default=list, blank=True)  # Store available days
    
    # Ratings and Reviews
    average_rating = models.DecimalField(max_digits=3, decimal_places=2, default=0.00)
    total_reviews = models.IntegerField(default=0)
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'doctors'
        verbose_name = 'Doctor'
        verbose_name_plural = 'Doctors'
        ordering = ['-average_rating', 'name']
    
    def __str__(self):
        return f"Dr. {self.name} - {self.get_specialty_display()}"
    
    @property
    def full_name(self):
        """Return the full name of the doctor."""
        return f"Dr. {self.name}"
    
    def update_rating(self):
        """Update doctor's average rating based on feedback."""
        from apps.appointments.models import AppointmentFeedback
        
        feedbacks = AppointmentFeedback.objects.filter(
            appointment__doctor=self
        ).exclude(overall_rating=0)
        
        if feedbacks.exists():
            self.average_rating = feedbacks.aggregate(
                avg_rating=models.Avg('overall_rating')
            )['avg_rating'] or 0.00
            self.total_reviews = feedbacks.count()
            self.save(update_fields=['average_rating', 'total_reviews'])


class DoctorSchedule(models.Model):
    """Doctor's schedule model."""
    
    DAY_CHOICES = [
        ('monday', 'Monday'),
        ('tuesday', 'Tuesday'),
        ('wednesday', 'Wednesday'),
        ('thursday', 'Thursday'),
        ('friday', 'Friday'),
        ('saturday', 'Saturday'),
        ('sunday', 'Sunday'),
    ]
    
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='schedules')
    day_of_week = models.CharField(max_length=10, choices=DAY_CHOICES)
    start_time = models.TimeField()
    end_time = models.TimeField()
    is_available = models.BooleanField(default=True)
    max_appointments = models.IntegerField(default=10)
    
    class Meta:
        db_table = 'doctor_schedules'
        verbose_name = 'Doctor Schedule'
        verbose_name_plural = 'Doctor Schedules'
        unique_together = ['doctor', 'day_of_week']
    
    def __str__(self):
        return f"{self.doctor.name} - {self.get_day_of_week_display()}"


class DoctorSpecialization(models.Model):
    """Doctor's specializations model."""
    
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='specializations')
    specialization = models.CharField(max_length=100)
    years_experience = models.IntegerField(default=0)
    is_primary = models.BooleanField(default=False)
    
    class Meta:
        db_table = 'doctor_specializations'
        verbose_name = 'Doctor Specialization'
        verbose_name_plural = 'Doctor Specializations'
    
    def __str__(self):
        return f"{self.doctor.name} - {self.specialization}"