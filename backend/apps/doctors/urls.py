from django.urls import path
from . import views

urlpatterns = [
    # Doctor CRUD
    path('', views.DoctorListView.as_view(), name='doctor-list'),
    path('<int:pk>/', views.DoctorDetailView.as_view(), name='doctor-detail'),
    path('create/', views.DoctorCreateView.as_view(), name='doctor-create'),
    path('<int:pk>/update/', views.DoctorUpdateView.as_view(), name='doctor-update'),
    
    # Doctor Features
    path('<int:doctor_id>/availability/<str:date>/', views.doctor_availability, name='doctor-availability'),
    path('<int:doctor_id>/stats/', views.doctor_stats, name='doctor-stats'),
    path('specialties/', views.doctor_specialties, name='doctor-specialties'),
    path('featured/', views.featured_doctors, name='featured-doctors'),
    path('search/', views.search_doctors, name='search-doctors'),
]