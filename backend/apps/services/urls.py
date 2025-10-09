from django.urls import path
from . import views

urlpatterns = [
    # Service CRUD
    path('', views.ServiceListView.as_view(), name='service-list'),
    path('<int:pk>/', views.ServiceDetailView.as_view(), name='service-detail'),
    path('create/', views.ServiceCreateView.as_view(), name='service-create'),
    path('<int:pk>/update/', views.ServiceUpdateView.as_view(), name='service-update'),
    
    # Service Features
    path('categories/', views.service_categories, name='service-categories'),
    path('packages/', views.service_packages, name='service-packages'),
    path('types/', views.service_types, name='service-types'),
    path('popular/', views.popular_services, name='popular-services'),
    path('search/', views.search_services, name='search-services'),
]