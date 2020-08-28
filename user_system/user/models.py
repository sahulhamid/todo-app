from django.db import models

# Create your models here

from django.contrib.auth.models import User
from django.utils import timezone

class Todo(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    tasked = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title
