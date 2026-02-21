from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Students(models.Model):
    name = models.CharField(max_length=10)
    age = models.IntegerField()
    email = models.EmailField()
    address = models.TextField()

    def __str__(self):
        return self.name
    
