from django.db import models

# Create your models here

from django.contrib.auth.models import User
from django.utils import timezone

class Todo(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    description=models.CharField(max_length=200,blank=True,null=True)
    completed = models.BooleanField(default=False)
    tasked = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.title

    def sdesc(self):
    	if len(self.description)<20:
    		return self.body

    	return self.description[0:20]+"..."		
