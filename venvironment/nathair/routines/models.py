from django.db import models
from django.contrib.auth import get_user_model
from products.models import HairProduct
from django.utils import timezone

User = get_user_model()

# Create your models here.
class Like(models.Model):
    ''' Defines Like model serving the HairRoutine model '''
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    routine = models.ForeignKey('HairRoutine', on_delete=models.CASCADE)


class Comment(models.Model):
    ''' Defines Comment model serving the HairRoutine model '''
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    routine = models.ForeignKey('HairRoutine', on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    parent_comment = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)


class HairRoutine(models.Model):
    ''' Defines the hair routine model '''
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    notes = models.TextField()
    is_draft = models.BooleanField(default=True)
    posted_at = models.DateTimeField(blank=True, null=True)
    likes = models.ManyToManyField(User, related_name='liked_routines', through=Like)

    def publish(self):
        self.is_draft = False
        self.posted_at = timezone.now()
        self.save()

    def num_saves(self):
        return self.savedroutine_set.count()

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


class SavedRoutine(models.Model):
    ''' Represents the relationship between users and saved routines '''
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    routine = models.ForeignKey(HairRoutine, on_delete=models.CASCADE)
    saved_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.user, self.routine)





