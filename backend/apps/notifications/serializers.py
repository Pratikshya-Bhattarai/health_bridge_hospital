from rest_framework import serializers
from .models import Notification, EmailTemplate


class NotificationSerializer(serializers.ModelSerializer):
    """Serializer for notifications."""
    
    class Meta:
        model = Notification
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at', 'sent_at', 'read_at')


class NotificationListSerializer(serializers.ModelSerializer):
    """Serializer for listing notifications."""
    
    class Meta:
        model = Notification
        fields = (
            'id', 'title', 'message', 'notification_type', 'priority',
            'is_read', 'is_sent', 'delivery_method', 'action_url',
            'created_at', 'read_at'
        )


class EmailTemplateSerializer(serializers.ModelSerializer):
    """Serializer for email templates."""
    
    class Meta:
        model = EmailTemplate
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')
