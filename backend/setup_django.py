#!/usr/bin/env python
"""
Django setup script for HealthBridge Hospital Backend
"""

import os
import sys
import django
from django.core.management import execute_from_command_line

def setup_django():
    """Setup Django project with initial data."""
    
    # Set Django settings
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'healthbridge_backend.settings')
    django.setup()
    
    print("🏥 Setting up HealthBridge Hospital Backend...")
    
    # Create migrations
    print("📝 Creating database migrations...")
    execute_from_command_line(['manage.py', 'makemigrations'])
    
    # Apply migrations
    print("🗄️ Applying database migrations...")
    execute_from_command_line(['manage.py', 'migrate'])
    
    # Create superuser
    print("👤 Creating superuser...")
    from django.contrib.auth import get_user_model
    User = get_user_model()
    
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser(
            username='admin',
            email='admin@healthbridge.com.np',
            password='admin123',
            user_type='admin',
            first_name='Admin',
            last_name='User'
        )
        print("✅ Superuser created: username='admin', password='admin123'")
    else:
        print("✅ Superuser already exists")
    
    # Create sample data
    print("📊 Creating sample data...")
    create_sample_data()
    
    print("🎉 Django setup completed successfully!")
    print("\n📋 Next steps:")
    print("1. Start the server: python manage.py runserver")
    print("2. Access admin: http://localhost:8000/admin/")
    print("3. View API docs: http://localhost:8000/api/docs/")
    print("4. Login: admin / admin123")

def create_sample_data():
    """Create sample data for testing."""
    from apps.doctors.models import Doctor
    from apps.services.models import Service
    from django.contrib.auth import get_user_model
    
    User = get_user_model()
    
    # Create sample doctors
    if not Doctor.objects.exists():
        doctors_data = [
            {
                'name': 'Dr. Suman Shrestha',
                'specialty': 'cardiology',
                'qualification': 'MBBS, MD (Cardiology)',
                'experience_years': 15,
                'consultation_fee': 1500.00,
                'bio': 'Specialist in angioplasty and bypass surgery with 15+ years of experience.'
            },
            {
                'name': 'Dr. Anjali Thapa',
                'specialty': 'neurology',
                'qualification': 'MBBS, MS (Neurosurgery)',
                'experience_years': 12,
                'consultation_fee': 1800.00,
                'bio': 'Expert in stroke care and brain surgeries, trained internationally.'
            },
            {
                'name': 'Dr. Rajesh Gurung',
                'specialty': 'orthopedics',
                'qualification': 'MBBS, MD (Orthopedics)',
                'experience_years': 18,
                'consultation_fee': 1200.00,
                'bio': 'Specialist in joint replacement and trauma care with advanced training.'
            },
            {
                'name': 'Dr. Priya Lama',
                'specialty': 'pediatrics',
                'qualification': 'MBBS, MD (Pediatrics)',
                'experience_years': 10,
                'consultation_fee': 1000.00,
                'bio': 'Expert in neonatal and child health care with compassionate approach.'
            }
        ]
        
        for doctor_data in doctors_data:
            # Create user for doctor
            user = User.objects.create_user(
                username=doctor_data['name'].lower().replace(' ', '_').replace('.', '').replace('dr_', ''),
                email=f"{doctor_data['name'].lower().replace(' ', '_').replace('.', '').replace('dr_', '')}@healthbridge.com.np",
                password='doctor123',
                user_type='doctor',
                first_name=doctor_data['name'].split()[1],
                last_name=doctor_data['name'].split()[2]
            )
            
            # Create doctor profile
            Doctor.objects.create(
                user=user,
                **doctor_data
            )
        
        print("✅ Sample doctors created")
    
    # Create sample services
    if not Service.objects.exists():
        services_data = [
            {
                'name': 'General Consultation',
                'description': 'General health checkup and consultation',
                'base_price': 1000.00,
                'duration_minutes': 30
            },
            {
                'name': 'Cardiology Consultation',
                'description': 'Heart and cardiovascular system consultation',
                'base_price': 1500.00,
                'duration_minutes': 45
            },
            {
                'name': 'Neurology Consultation',
                'description': 'Brain and nervous system consultation',
                'base_price': 1800.00,
                'duration_minutes': 45
            },
            {
                'name': 'Orthopedics Consultation',
                'description': 'Bone and joint consultation',
                'base_price': 1200.00,
                'duration_minutes': 30
            },
            {
                'name': 'Pediatrics Consultation',
                'description': 'Child health consultation',
                'base_price': 1000.00,
                'duration_minutes': 30
            },
            {
                'name': 'Emergency Consultation',
                'description': 'Urgent medical consultation',
                'base_price': 2000.00,
                'duration_minutes': 60
            }
        ]
        
        for service_data in services_data:
            Service.objects.create(**service_data)
        
        print("✅ Sample services created")

if __name__ == '__main__':
    setup_django()