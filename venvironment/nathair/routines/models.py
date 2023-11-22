from django.db import models
from django.contrib.auth import get_user_model
from products.models import HairProduct

User = get_user_model()

# Create your models here.
class HairRoutine(models.Model):
    ''' Defines the hair routine model '''
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    notes = models.TextField()

    def __str__(self):
        return '%s - %s' % (self.name, self.user)
    

class RoutineStep(models.Model):
    ''' Defines the routine step model serving the hair routine model '''
    hair_routine = models.ForeignKey(HairRoutine, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    product = models.ForeignKey(HairProduct, on_delete=models.CASCADE)

    def __str__(self):
        return '%s - %s' % (self.title, self.hair_routine)