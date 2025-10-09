from rest_framework import generics, status, permissions, filters
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Q, Avg, Count
from .models import Service, ServiceCategory, ServicePackage
from .serializers import (
    ServiceSerializer, ServiceListSerializer, ServiceCreateSerializer,
    ServiceUpdateSerializer, ServiceCategorySerializer, ServicePackageSerializer
)


class ServiceListView(generics.ListAPIView):
    """List all services with filtering and search."""
    
    serializer_class = ServiceListSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['service_type', 'is_available', 'requires_appointment']
    search_fields = ['name', 'description', 'tags']
    ordering_fields = ['name', 'base_price', 'duration_minutes', 'created_at']
    ordering = ['name']
    
    def get_queryset(self):
        return Service.objects.filter(is_available=True)


class ServiceDetailView(generics.RetrieveAPIView):
    """Get service details."""
    
    serializer_class = ServiceSerializer
    permission_classes = [permissions.AllowAny]
    queryset = Service.objects.all()


class ServiceCreateView(generics.CreateAPIView):
    """Create a new service (admin/staff only)."""
    
    serializer_class = ServiceCreateSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def perform_create(self, serializer):
        if self.request.user.user_type not in ['admin', 'staff']:
            raise permissions.PermissionDenied("Only admin and staff can create services")
        serializer.save()


class ServiceUpdateView(generics.UpdateAPIView):
    """Update service information."""
    
    serializer_class = ServiceUpdateSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Service.objects.all()
    
    def get_object(self):
        service = super().get_object()
        if self.request.user.user_type not in ['admin', 'staff']:
            raise permissions.PermissionDenied("Only admin and staff can update services")
        return service


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def service_categories(request):
    """Get list of service categories."""
    categories = ServiceCategory.objects.filter(is_active=True)
    serializer = ServiceCategorySerializer(categories, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def service_packages(request):
    """Get list of active service packages."""
    packages = ServicePackage.objects.filter(is_active=True)
    serializer = ServicePackageSerializer(packages, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def service_types(request):
    """Get list of available service types."""
    service_types = Service.SERVICE_TYPE_CHOICES
    return Response([{'value': choice[0], 'label': choice[1]} for choice in service_types])


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def popular_services(request):
    """Get popular services based on bookings."""
    from apps.appointments.models import Appointment
    
    # Get services with most appointments
    popular_service_ids = Appointment.objects.filter(
        status__in=['completed', 'confirmed']
    ).values('service').annotate(
        booking_count=Count('service')
    ).order_by('-booking_count')[:6]
    
    service_ids = [item['service'] for item in popular_service_ids]
    services = Service.objects.filter(id__in=service_ids, is_available=True)
    
    serializer = ServiceListSerializer(services, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def search_services(request):
    """Search services by name, description, or tags."""
    query = request.GET.get('q', '')
    service_type = request.GET.get('type', '')
    max_price = request.GET.get('max_price', None)
    min_duration = request.GET.get('min_duration', None)
    
    queryset = Service.objects.filter(is_available=True)
    
    if query:
        queryset = queryset.filter(
            Q(name__icontains=query) |
            Q(description__icontains=query) |
            Q(tags__icontains=query)
        )
    
    if service_type:
        queryset = queryset.filter(service_type=service_type)
    
    if max_price:
        queryset = queryset.filter(base_price__lte=float(max_price))
    
    if min_duration:
        queryset = queryset.filter(duration_minutes__gte=int(min_duration))
    
    serializer = ServiceListSerializer(queryset, many=True)
    return Response(serializer.data)