from django.db import models
from datetime import datetime
# Create your models here.
class Room(models.Model):
    name=models.CharField(max_length=255)

class Message(models.Model):
    text=models.CharField(max_length=255)
    date=models.DateTimeField(default= datetime.now,blank=True)
    username=models.CharField(max_length=255)
    room_name=models.CharField(max_length=255)

