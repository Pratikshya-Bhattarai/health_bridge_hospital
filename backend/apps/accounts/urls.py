from django.urls import path
from . import views

urlpatterns = [
    # Authentication
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    
    # Profile Management
    path('profile/', views.user_profile, name='user-profile'),
    path('profile/update/', views.UserProfileView.as_view(), name='profile-update'),
    path('profile/detail/', views.UserProfileDetailView.as_view(), name='profile-detail'),
    
    # Password Management
    path('change-password/', views.change_password, name='change-password'),
    path('password-reset/', views.password_reset_request, name='password-reset'),
    path('password-reset-confirm/<str:uidb64>/<str:token>/', views.password_reset_confirm, name='password-reset-confirm'),
    
    # User Management (Admin/Staff)
    path('users/', views.UserListView.as_view(), name='user-list'),
    path('stats/', views.user_stats, name='user-stats'),
]