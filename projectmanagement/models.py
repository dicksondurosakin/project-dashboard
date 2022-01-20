from email.policy import default
from django.db import models
from django.utils import timezone
from datetime import datetime,timedelta

# Create your models here.
class Project(models.Model):
    STATUS_CHOICES = (
        ('a','ongoing'),
        ('c','stalled'),
        ('b','completed')
    )
    title = models.CharField(max_length=256)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    first_contributor = models.ImageField(upload_to = 'users/%Y/%m/%d/',default='/female_image.png')
    second_contributor = models.ImageField(upload_to = 'users/%Y/%m/%d/',default='/female_image.png')
    third_contributor = models.ImageField(upload_to = 'users/%Y/%m/%d/',default='/female_image.png')
    status = models.CharField(max_length=15,choices=STATUS_CHOICES)

    @property
    def active(self):
        last_active = datetime(self.updated.year, self.updated.month, self.updated.day, self.updated.hour+1, self.updated.minute, self.updated.second, self.updated.microsecond)
        return last_active.strftime("%H:%M")

    class Meta:
        ordering = ('status',)
    
    def __str__(self):
        return self.title

class Task(models.Model):
    name = models.CharField(max_length=256)
    owner = models.ForeignKey(Project,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
