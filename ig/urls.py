from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

# URL Configurations
urlpatterns = [
    path("", views.login_request, name="login"),
    path("homepage", views.homepage, name="homepage"),
    path("register/", views.register_request, name="register"),
    path("login/", views.login_request, name="login"),
    path("logout/", views.logout_request, name= "logout"),
    path('profile/', views.profile,name = 'profile'),
    path("post", views.post, name="post"),
    path('edit_profile/', views.edit_profile,name = 'edit_profile'),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)