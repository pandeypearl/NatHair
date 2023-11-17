"""
    Models for accounts application
"""
from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

# User Confirmation.
class Profile(models.Model):
    ''' Defines user profile model '''
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics', default='blank-profile-pic.png')
    location = models.CharField(max_length=255, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.user.username


class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.IntegerField()
    bio = models.TextField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics', default='blank-profile-pic.png')
    location = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.user.username


# User Hair Profile Model
class HairProfile(models.Model):
    """
        Hair profile model extending user model using
        one-to-one link.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
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

    def __str__(self):
        return  self.user.username + self.hair_type + self.hair_porosity + self.hair_condition + self.hair_length 

