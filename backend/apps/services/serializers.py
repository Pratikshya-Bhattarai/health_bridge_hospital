from rest_framework import serializers
from .models import Service, ServiceCategory, ServicePackage


class ServiceSerializer(serializers.ModelSerializer):
    """Serializer for services."""
    
    class Meta:
        model = Service
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')


class ServiceListSerializer(serializers.ModelSerializer):
    """Serializer for listing services."""
    
    class Meta:
        model = Service
        fields = (
            'id', 'name', 'description', 'service_type', 'base_price',
            'duration_minutes', 'is_available', 'image'
        )


class ServiceCategorySerializer(serializers.ModelSerializer):
    """Serializer for service categories."""
    
    class Meta:
        model = ServiceCategory
        fields = '__all__'


class ServicePackageSerializer(serializers.ModelSerializer):
    """Serializer for service packages."""
    
    services = ServiceListSerializer(many=True, read_only=True)
    final_price = serializers.ReadOnlyField()
    
    class Meta:
        model = ServicePackage
        fields = '__all__'


class ServiceCreateSerializer(serializers.ModelSerializer):
    """Serializer for creating services."""
    
    class Meta:
        model = Service
        fields = (
            'name', 'description', 'service_type', 'base_price',
            'duration_minutes', 'requirements', 'preparation_instructions',
            'what_to_expect', 'follow_up_required', 'is_available',
            'requires_appointment', 'max_daily_appointments', 'tags'
        )


class ServiceUpdateSerializer(serializers.ModelSerializer):
    """Serializer for updating services."""
    
    class Meta:
        model = Service
        fields = (
            'name', 'description', 'service_type', 'base_price',
            'duration_minutes', 'requirements', 'preparation_instructions',
            'what_to_expect', 'follow_up_required', 'is_available',
            'requires_appointment', 'max_daily_appointments', 'tags'
        )