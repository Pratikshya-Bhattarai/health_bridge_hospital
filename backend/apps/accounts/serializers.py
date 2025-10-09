from rest_framework import serializers
from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password
from .models import User, UserProfile


class UserRegistrationSerializer(serializers.ModelSerializer):
    """Serializer for user registration."""
    
    password = serializers.CharField(write_only=True, validators=[validate_password])
    password_confirm = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields = (
            'username', 'email', 'password', 'password_confirm', 'user_type',
            'first_name', 'last_name', 'phone_number', 'date_of_birth', 'gender',
            'address', 'emergency_contact', 'emergency_contact_name'
        )
        extra_kwargs = {
            'password': {'write_only': True},
            'password_confirm': {'write_only': True},
        }
    
    def validate(self, attrs):
        if attrs['password'] != attrs['password_confirm']:
            raise serializers.ValidationError("Passwords don't match")
        return attrs
    
    def create(self, validated_data):
        validated_data.pop('password_confirm')
        user = User.objects.create_user(**validated_data)
        
        # Create user profile
        UserProfile.objects.create(user=user)
        
        return user


class UserLoginSerializer(serializers.Serializer):
    """Serializer for user login."""
    
    username = serializers.CharField()
    password = serializers.CharField()
    
    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')
        
        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise serializers.ValidationError('Invalid credentials')
            if not user.is_active:
                raise serializers.ValidationError('User account is disabled')
            attrs['user'] = user
            return attrs
        else:
            raise serializers.ValidationError('Must include username and password')


class UserProfileSerializer(serializers.ModelSerializer):
    """Serializer for user profile."""
    
    full_name = serializers.CharField(source='get_full_name', read_only=True)
    profile = serializers.SerializerMethodField()
    
    class Meta:
        model = User
        fields = (
            'id', 'username', 'email', 'first_name', 'last_name', 'full_name',
            'user_type', 'phone_number', 'date_of_birth', 'gender', 'address',
            'emergency_contact', 'emergency_contact_name', 'profile_image',
            'bio', 'is_verified', 'is_active', 'created_at', 'updated_at',
            'last_login', 'profile'
        )
        read_only_fields = ('id', 'username', 'created_at', 'updated_at', 'last_login')
    
    def get_profile(self, obj):
        try:
            profile = obj.profile
            return UserProfileDetailSerializer(profile).data
        except UserProfile.DoesNotExist:
            return None


class UserProfileDetailSerializer(serializers.ModelSerializer):
    """Serializer for detailed user profile."""
    
    class Meta:
        model = UserProfile
        fields = (
            'blood_type', 'allergies', 'medical_conditions', 'current_medications',
            'insurance_provider', 'insurance_number', 'insurance_expiry',
            'preferred_language', 'notification_preferences', 'created_at', 'updated_at'
        )
        read_only_fields = ('created_at', 'updated_at')


class UserUpdateSerializer(serializers.ModelSerializer):
    """Serializer for updating user information."""
    
    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'email', 'phone_number', 'date_of_birth',
            'gender', 'address', 'emergency_contact', 'emergency_contact_name',
            'profile_image', 'bio'
        )


class UserListSerializer(serializers.ModelSerializer):
    """Serializer for listing users."""
    
    full_name = serializers.CharField(source='get_full_name', read_only=True)
    
    class Meta:
        model = User
        fields = (
            'id', 'username', 'full_name', 'email', 'user_type', 'phone_number',
            'is_active', 'is_verified', 'created_at'
        )


class PasswordChangeSerializer(serializers.Serializer):
    """Serializer for password change."""
    
    old_password = serializers.CharField()
    new_password = serializers.CharField(validators=[validate_password])
    new_password_confirm = serializers.CharField()
    
    def validate(self, attrs):
        if attrs['new_password'] != attrs['new_password_confirm']:
            raise serializers.ValidationError("New passwords don't match")
        return attrs
    
    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError("Old password is incorrect")
        return value


class PasswordResetSerializer(serializers.Serializer):
    """Serializer for password reset request."""
    
    email = serializers.EmailField()
    
    def validate_email(self, value):
        try:
            User.objects.get(email=value, is_active=True)
        except User.DoesNotExist:
            raise serializers.ValidationError("No active user found with this email address")
        return value


class PasswordResetConfirmSerializer(serializers.Serializer):
    """Serializer for password reset confirmation."""
    
    token = serializers.CharField()
    new_password = serializers.CharField(validators=[validate_password])
    new_password_confirm = serializers.CharField()
    
    def validate(self, attrs):
        if attrs['new_password'] != attrs['new_password_confirm']:
            raise serializers.ValidationError("Passwords don't match")
        return attrs