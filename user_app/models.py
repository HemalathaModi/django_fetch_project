from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=255)
    age = models.PositiveIntegerField()

    class Meta:
        db_table = 'Profile'

    def __str__(self):
        return self.user.username

# Create your models here.
