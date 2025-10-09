from rest_framework import serializers
from .models import Doctor, DoctorSchedule, DoctorSpecialization


class DoctorScheduleSerializer(serializers.ModelSerializer):
    """Serializer for doctor schedules."""
    
    class Meta:
        model = DoctorSchedule
        fields = '__all__'


class DoctorSpecializationSerializer(serializers.ModelSerializer):
    """Serializer for doctor specializations."""
    
    class Meta:
        model = DoctorSpecialization
        fields = '__all__'


class DoctorSerializer(serializers.ModelSerializer):
    """Serializer for doctors."""
    
    full_name = serializers.CharField(source='get_full_name', read_only=True)
    schedules = DoctorScheduleSerializer(many=True, read_only=True)
    specializations = DoctorSpecializationSerializer(many=True, read_only=True)
    
    class Meta:
        model = Doctor
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at', 'average_rating', 'total_reviews')


class DoctorListSerializer(serializers.ModelSerializer):
    """Serializer for listing doctors."""
    
    full_name = serializers.CharField(source='get_full_name', read_only=True)
    specialty_display = serializers.CharField(source='get_specialty_display', read_only=True)
    
    class Meta:
        model = Doctor
        fields = (
            'id', 'name', 'full_name', 'specialty', 'specialty_display',
            'qualification', 'experience_years', 'consultation_fee',
            'average_rating', 'total_reviews', 'is_available',
            'profile_image'
        )


class DoctorDetailSerializer(serializers.ModelSerializer):
    """Serializer for doctor details."""
    
    full_name = serializers.CharField(source='get_full_name', read_only=True)
    schedules = DoctorScheduleSerializer(many=True, read_only=True)
    specializations = DoctorSpecializationSerializer(many=True, read_only=True)
    
    class Meta:
        model = Doctor
        fields = '__all__'


class DoctorCreateSerializer(serializers.ModelSerializer):
    """Serializer for creating doctors."""
    
    class Meta:
        model = Doctor
        fields = (
            'name', 'specialty', 'qualification', 'experience_years',
            'consultation_fee', 'license_number', 'medical_council',
            'bio', 'education', 'certifications', 'phone_number',
            'email', 'address', 'gender', 'date_of_birth'
        )
    
    def create(self, validated_data):
        # Create user for doctor
        from django.contrib.auth import get_user_model
        User = get_user_model()
        
        user = User.objects.create_user(
            username=validated_data['name'].lower().replace(' ', '_'),
            email=validated_data.get('email', ''),
            password='doctor123',  # Default password
            user_type='doctor',
            first_name=validated_data['name'].split()[0],
            last_name=' '.join(validated_data['name'].split()[1:]) if len(validated_data['name'].split()) > 1 else ''
        )
        
        validated_data['user'] = user
        return super().create(validated_data)


class DoctorUpdateSerializer(serializers.ModelSerializer):
    """Serializer for updating doctors."""
    
    class Meta:
        model = Doctor
        fields = (
            'name', 'specialty', 'qualification', 'experience_years',
            'consultation_fee', 'bio', 'education', 'certifications',
            'phone_number', 'email', 'address', 'gender', 'date_of_birth',
            'is_available', 'working_hours', 'available_days'
        )


class DoctorStatsSerializer(serializers.Serializer):
    """Serializer for doctor statistics."""
    
    total_appointments = serializers.IntegerField()
    completed_appointments = serializers.IntegerField()
    pending_appointments = serializers.IntegerField()
    cancelled_appointments = serializers.IntegerField()
    total_revenue = serializers.DecimalField(max_digits=10, decimal_places=2)
    average_rating = serializers.DecimalField(max_digits=3, decimal_places=2)
    total_reviews = serializers.IntegerField()
    next_appointment = serializers.DateTimeField(allow_null=True)