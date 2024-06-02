from django.urls import path
from .views import register_admin, register_agent, register_user

urlpatterns = [
    path('registerUser/', register_user),
    path('registerAgent/', register_agent),
    path('registerAdmin/', register_admin),
]
