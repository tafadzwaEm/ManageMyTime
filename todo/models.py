from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Todo(models.Model):
    todoname = models.CharField(max_length=300)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.todoname
    
    def get_absolute_url(self):
        return reverse('home')

class Upcoming(models.Model):
    eventname = models.CharField(max_length=300)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.eventname

    def get_absolute_url(self):
        return reverse('home')

