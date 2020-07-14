from django.db import models
from django import forms
from django.utils import timezone

# Create your models here.
class Task(models.Model):
    title=models.CharField(max_length=200)
    tasks=models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    date=models.DateTimeField(default=timezone.now)
    
    def __str__(self):

        return self.title+" "
