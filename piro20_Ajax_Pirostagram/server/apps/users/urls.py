from django.urls import path
from . import views

# from .views import CustomSignupView
app_name = "users"

urlpatterns = [
    path("logout/", views.logout, name="logout"),
]