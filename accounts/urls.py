from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('admin/', views.admin, name='admin'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
]
