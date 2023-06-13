"""
    Models for accounts application
"""
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# User Confirmation.
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
        Django signal for when new user is created in User model,
        signal will be triggered and user details will be added to Profile
        model with default django  email confirmed as false.
    """
    if created:
        Profile.objects.create(user=instance)
        instance.profile.save()

# User Hair Profile Model
class HairProfile(models.Model):
    """
        Hair profile model extending user model using
        one-to-one link.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Specifying Hair Type Choices
    TYPE_CHOICES = (
        ("1a", "1a"),
        ("1b", "1b"),
        ("1c", "1c"),
        ("2a", "2a"),
        ("2b", "2b"),
        ("2c", "2c"),
        ("3a", "3a"),
        ("3b", "3b"),
        ("3c", "3c"),
        ("4a", "4a"),
        ("4b", "4b"),
        ("4c", "4c"),
    )
    hair_type = models.CharField(
        max_length = 2,
        choices = TYPE_CHOICES,
        default="4c"
    )

    # Specifying Hair Porosity Choices
    POROSITY_CHOICES = (
        ("low", "Low Porosity"),
        ("medium", "Medium Porosity"),
        ("high", "Hight Porosity"),
    )
    hair_porosity = models.CharField(
        max_length=6,
        choices= POROSITY_CHOICES,
        default="low"
    )

    # Specifying Hair Condition Choices
    CONDITION_CHOICES = (
        ("protein_overload", "Protein Overload"),
        ("moisture_overload", "Moisture Overload"),
        ("healthy", "Healthy"),
        ("dandruff", "Dandruff"),
        ("hair_loss", "Hair Loss"),
        ("dry_hair", "Dry Hair"),
        ("split_ends", "Split Ends"),
        ("greasy", "Greasy Hair"),
        ("frizzy", "Frizzy"),
        ("heat_damage", "Heat Damage"),
        ("color_damage", "Color Damage")
    )
    hair_condition = models.CharField(
        max_length=20,
        choices= CONDITION_CHOICES,
        default="protein_overload"
    )
    # Specifying Hair Length Choices
    LENGTH_CHOICES = (
        ("ear", "Ear Length"),
        ("necktop", "Neck (top) Length"),
        ("neckbottom", "Neck (bottom) Length"),
        ("collarbone", "Collarbone Length"),
        ("shoulder", "Shoulder Length"),
        ("armpit", "Armpit Length"),
        ("brastrap", "Bra Strap Length"),
        ("midback", "Mid Back Length"),
        ("waist", "Waist Length"),
        ("hip", "Hip Length"),
        ("tailbone", "Tailbone Length"),
        ("classic", "Classic Length"),
        ("midthigh", "Mid Thigh Length"),
        ("knee", "Knee Length"),
        ("calf", "Calf Length"),
        ("ankle", "Ankle Length"),
        ("floor", "Floor Length"),
    )
    hair_length = models.CharField(
        max_length=20,
        choices= LENGTH_CHOICES,
        default="ear"
    )


@receiver(post_save, sender=User)
def create_hair_profile(sender, instance, created, **kwargs):
    """
        Defining signals so Hair Profile model will be created/updated
        automatically when the User instance is created and updated.
    """
    if created:
        HairProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    """
        Save event to linking the create_hair_profile and 
        save_hair_profile methods to User model. 
    """
    instance.hairprofile.save()


