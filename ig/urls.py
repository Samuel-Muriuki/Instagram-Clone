from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

# URL Configurations
urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("register/", views.register_request, name="register"),
    path("login/", views.login_request, name="login"),
    path("logout/", views.logout_request, name= "logout"),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)