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
    '''
        Hair profile model extending user model using
        one-to-one link.
    '''
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
        choices = TYPE_CHOICES
    )

    # Specifying Hair Porosity Choices
    POROSITY_CHOICES = (
        ("Low Porosity", "Low Porosity"),
        ("Medium Porosity", "Medium Porosity"),
        ("Hight Porosity", "Hight Porosity"),
    )
    hair_porosity = models.CharField(
        max_length=20,
        choices= POROSITY_CHOICES
    )

    # Specifying Hair Condition Choices
    CONDITION_CHOICES = (
        ("Protein Overload", "Protein Overload"),
        ("Moisture Overload", "Moisture Overload"),
        ("Healthy", "Healthy"),
        ("Dandruff", "Dandruff"),
        ("Hair Loss", "Hair Loss"),
        ("Dry Hair", "Dry Hair"),
        ("Split Ends", "Split Ends"),
        ("Greasy Hair", "Greasy Hair"),
        ("Frizzy", "Frizzy"),
        ("Heat Damage", "Heat Damage"),
        ("Color Damage", "Color Damage")
    )
    hair_condition = models.CharField(
        max_length=20,
        choices= CONDITION_CHOICES
    )
    # Specifying Hair Length Choices
    LENGTH_CHOICES = (
        ("Ear Length", "Ear Length"),
        ("Neck (top) Length", "Neck (top) Length"),
        ("Neck (bottom) Length", "Neck (bottom) Length"),
        ("Collarbone Length", "Collarbone Length"),
        ("Shoulder Length", "Shoulder Length"),
        ("Armpit Length", "Armpit Length"),
        ("Bra Strap Length", "Bra Strap Length"),
        ("Mid Back Length", "Mid Back Length"),
        ("Waist Length", "Waist Length"),
        ("Hip Length", "Hip Length"),
        ("Tailbone Length", "Tailbone Length"),
        ("Classic Length", "Classic Length"),
        ("Mid Thigh Length", "Mid Thigh Length"),
        ("Knee Length", "Knee Length"),
        ("Calf Length", "Calf Length"),
        ("Ankle Length", "Ankle Length"),
        ("Floor Length", "Floor Length"),
    )
    hair_length = models.CharField(
        max_length=20,
        choices= LENGTH_CHOICES
    )

    def __str__(self):
        return  self.user.username


class TextureProfile(models.Model):
    '''
        Hair texture profile model extending user model using
        one-to-one link.
    '''
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    wet_hair = models.ImageField(upload_to='wet_hair_pics', blank=True, null=True, default='blank-profile-pic.png')
    dry_hair = models.ImageField(upload_to='dry_hair_pics', blank=True, null=True, default='blank-profile-pic.png')
    wet_hair_prod = models.ImageField(upload_to='wet_hair_product_pics', blank=True, null=True, default='blank-profile-pic.png')
    dry_hair_prod = models.ImageField(upload_to='dry_hair_product_pics', blank=True, null=True, default='blank-profile-pic.png')

    def __str__(self):
        return self.user.username