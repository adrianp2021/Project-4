from django.db import models
from django.contrib.auth.models import AbstractUser
from interests.models import Interest

class User(AbstractUser):
    profile_image = models.CharField(max_length=500, default=None)
    email = models.CharField(max_length=50, unique=True)
    preferences = [
        ('ME', 'Men'), 
        ('WO', 'Women'), 
        ('BI', 'Bisexual')
    ]
    preferences = models.CharField(
      max_length=20,
      choices=preferences,
      null=True
    )
    interests = models.ManyToManyField(
      Interest
    )
    age = models.PositiveIntegerField(default=None)
    def __str__(self):
        return f"{self.username}"
