from django.db import models
from django.utils.translation import gettext_lazy as _
from users.models import Roles, RolesChoices

class AccessControlChoice(models.TextChoices):
        title = 'title', _('title')
        description = 'description', _('description')
        gearns = 'gearns', _('gearns')
        cast = 'cast', _('cast')
        crew = 'crew', _('crew')

class Celebrities(models.Model):
    name = models.CharField()

class Grarns(models.Model):
    name = models.CharField()

class Crew(models.Model):
    director = models.ManyToManyField(Celebrities),
    producer = models.ManyToManyField(Celebrities),
    writer  = models.ManyToManyField(Celebrities)

class AccessControl(models.Model):
   role=models.ForeignKey(Roles, on_delete=models.CASCADE)
   controlChoice = models.CharField(max_length=100,choices=AccessControlChoice.choices,
        default=AccessControlChoice.title)

class TelevisionShow(models.Model):
    title = models.CharField(max_length=100,)
    description = models.TextField()
    release_date = models.DateField()
    gearns = models.ManyToManyField(Grarns)
    cast =  models.ManyToManyField(Celebrities)
    crew = models.OneToOneField(Crew)
    access_control = models.ManyToManyField(AccessControl)