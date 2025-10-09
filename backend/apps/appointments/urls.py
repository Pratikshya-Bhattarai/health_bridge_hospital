from django.urls import path
from . import views

urlpatterns = [
    # Appointment CRUD
    path('', views.AppointmentListView.as_view(), name='appointment-list'),
    path('<int:pk>/', views.AppointmentDetailView.as_view(), name='appointment-detail'),
    path('create/', views.AppointmentCreateView.as_view(), name='appointment-create'),
    path('<int:pk>/update/', views.AppointmentUpdateView.as_view(), name='appointment-update'),
    
    # Appointment Actions
    path('<int:appointment_id>/cancel/', views.cancel_appointment, name='cancel-appointment'),
    path('<int:appointment_id>/confirm/', views.confirm_appointment, name='confirm-appointment'),
    
    # Appointment Features
    path('available-slots/<int:doctor_id>/<str:date>/', views.available_slots, name='available-slots'),
    path('stats/', views.appointment_stats, name='appointment-stats'),
    path('<int:appointment_id>/feedback/', views.add_feedback, name='add-feedback'),
    path('<int:appointment_id>/upload-document/', views.upload_document, name='upload-document'),
]