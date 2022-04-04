from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profile_info = models.TextField()
    picture = models.ImageField(upload_to='post/', blank=True,default='')
    name = models.CharField(max_length=50)

    