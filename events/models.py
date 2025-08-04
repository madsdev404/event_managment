from django.db import models
from users.models import CustomUser

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    organizer = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='organized_categories', null=True, blank=True)

    def __str__(self):
        return self.name

class Event(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    participants = models.ManyToManyField(CustomUser, related_name='events', blank=True)
    image = models.ImageField(upload_to='event_images/', default='event_images/default.jpg')
    organizer = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='organized_events', null=True, blank=True)

    def __str__(self):
        return self.name
