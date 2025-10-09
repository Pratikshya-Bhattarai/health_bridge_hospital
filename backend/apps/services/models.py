from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Service(models.Model):
    """Medical service model."""
    
    SERVICE_TYPE_CHOICES = [
        ('consultation', 'Consultation'),
        ('diagnostic', 'Diagnostic'),
        ('treatment', 'Treatment'),
        ('surgery', 'Surgery'),
        ('emergency', 'Emergency'),
        ('preventive', 'Preventive Care'),
        ('rehabilitation', 'Rehabilitation'),
    ]
    
    DURATION_CHOICES = [
        (15, '15 minutes'),
        (30, '30 minutes'),
        (45, '45 minutes'),
        (60, '1 hour'),
        (90, '1.5 hours'),
        (120, '2 hours'),
    ]
    
    # Basic Information
    name = models.CharField(max_length=200)
    description = models.TextField()
    service_type = models.CharField(max_length=20, choices=SERVICE_TYPE_CHOICES, default='consultation')
    
    # Pricing and Duration
    base_price = models.DecimalField(max_digits=10, decimal_places=2)
    duration_minutes = models.IntegerField(choices=DURATION_CHOICES, default=30)
    
    # Service Details
    requirements = models.TextField(blank=True)
    preparation_instructions = models.TextField(blank=True)
    what_to_expect = models.TextField(blank=True)
    follow_up_required = models.BooleanField(default=False)
    
    # Availability
    is_available = models.BooleanField(default=True)
    requires_appointment = models.BooleanField(default=True)
    max_daily_appointments = models.IntegerField(default=20)
    
    # Additional Information
    image = models.ImageField(upload_to='services/', blank=True, null=True)
    tags = models.JSONField(default=list, blank=True)  # Store service tags
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'services'
        verbose_name = 'Service'
        verbose_name_plural = 'Services'
        ordering = ['name']
    
    def __str__(self):
        return self.name


class ServiceCategory(models.Model):
    """Service category model."""
    
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    icon = models.CharField(max_length=50, blank=True)  # Icon class name
    is_active = models.BooleanField(default=True)
    sort_order = models.IntegerField(default=0)
    
    class Meta:
        db_table = 'service_categories'
        verbose_name = 'Service Category'
        verbose_name_plural = 'Service Categories'
        ordering = ['sort_order', 'name']
    
    def __str__(self):
        return self.name


class ServicePackage(models.Model):
    """Service package model for bundled services."""
    
    name = models.CharField(max_length=200)
    description = models.TextField()
    services = models.ManyToManyField(Service, related_name='packages')
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_percentage = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    is_active = models.BooleanField(default=True)
    valid_from = models.DateField()
    valid_until = models.DateField(null=True, blank=True)
    
    class Meta:
        db_table = 'service_packages'
        verbose_name = 'Service Package'
        verbose_name_plural = 'Service Packages'
    
    def __str__(self):
        return self.name
    
    @property
    def final_price(self):
        """Calculate final price after discount."""
        discount_amount = (self.total_price * self.discount_percentage) / 100
        return self.total_price - discount_amount