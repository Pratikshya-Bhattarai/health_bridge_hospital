from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.PatientDetailView.as_view(), name='patient-profile'),
    path('dashboard/', views.patient_dashboard, name='patient-dashboard'),
    path('medical-records/', views.MedicalRecordListView.as_view(), name='medical-records'),
    path('medical-records/<int:pk>/', views.MedicalRecordDetailView.as_view(), name='medical-record-detail'),
]