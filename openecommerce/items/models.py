from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=75)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    
    def __str__(self):
        return self.name
    