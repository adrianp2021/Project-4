from django.db import models
from interests.models import Interest

# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=50)
    profile_image = models.CharField(max_length=500, default=None)
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
