from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('membership', views.membership, name='membership'),
    path('profile', views.profile, name='profile'),
    path('status', views.status, name='status'),
    path('application', views.application, name='application'),
]