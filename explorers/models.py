from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User


class Assembly(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title_of_activity = models.CharField(max_length=255, blank=True)
    activity = models.TextField(max_length=200, blank=True)
   
    def __str__(self):
        return self.name


def create_assembly(sender, instance, created, **kwargs):
    if created:
        Assembly.objects.create(name=instance)


post_save.connect(create_assembly, sender=User)