"""
    Models for accounts application
"""
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Profile(models.Model):
    """
        Profile model to determine if there has been email confirmation
        for a new signup.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email_confirmed = models.BooleanField(default=False)

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    """
        django signal for when new user is created in User model,
        signal will be triggered and user details will be added to Profile
        model with default django  email confirmed as false.
    """
    if created:
        Profile.objects.create(user=instance)
        instance.profile.save()

