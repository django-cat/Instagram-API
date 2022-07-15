from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class User(AbstractUser):
    followers = models.ManyToManyField('self', symmetrical = False, related_name = 'followings', blank = True)

class Profile(models.Model):
    genders = [
        ('male', 'male'),
        ('female', 'female')
    ]
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name = 'profile', on_delete = models.CASCADE)
    name = models.TextField(blank = True, null = True)
    gender = models.CharField(max_length = 6, choices = genders)
    introduction = models.TextField(blank = True, null = True)
    image = models.ImageField(upload_to = 'profile/', blank = True, null = True)