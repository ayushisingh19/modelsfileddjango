from django.db import models
from datetime import time
from datetime import date


# Create your models here.

class userproflile(models.Model):
    quali=[('1',"b.etch"),('2',"m.tch"),('3',"bcom")]
    username=models.CharField(max_length=30, null=True ,unique=True,blank=False,help_text="enter a unquie username")
    email=models.CharField(max_length=255, unique=True,blank=False)
    bio=models.CharField(max_length=50,blank=True,null=True, help_text="write a short bio about yourself")
    is_active=models.BooleanField(default=False)
    qualification=models.CharField(max_length=100,choices=quali,null=True,verbose_name='quali',db_index=True)
    remark=models.TextField(max_length=100,null=True,blank=True)
    def __str__(self):
        return str(self.username)

class Shift(models.Model):
    name = models.CharField(max_length=100)
    start_time = models.TimeField(help_text="Shift start time.")
    end_time = models.TimeField(null=True, blank=True, verbose_name="Shift End Time")
    created_at = models.TimeField(auto_now_add=True)
    last_updated = models.TimeField(auto_now=True)

class Event(models.Model):
    name = models.CharField(max_length=100)
    event_date = models.DateField(help_text="Enter the event date.")
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    deadline = models.DateField(default=date.today, verbose_name="Submission Deadline")