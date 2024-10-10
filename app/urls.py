# licenses/urls.py
from django.urls import path
from .views import create_license, license_list, validate_license, revoke_license, register, base
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', base, name='home'),
    path('create/', create_license, name='create_license'),
    path('list/', license_list, name='license_list'),
    path('licenses/revoke/<str:key>/', revoke_license, name='revoke_license'),
    path('validate/<str:key>/', validate_license, name='validate_license'),
    path('revoke/<str:key>/', revoke_license, name='revoke_license'),
    path('register/', register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='licenses/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
