from django.urls import path
from . import views

# URL Configurations
urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("register", views.register_request, name="register")
]