from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Contact(models.Model):
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    country_code = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=30)
    contact_picture = models.ImageField(upload_to='post_images', null=True)
    is_favourite = models.BooleanField(default=False)
