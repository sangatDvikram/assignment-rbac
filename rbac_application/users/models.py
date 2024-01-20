from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
from django.contrib.auth.models import User

class RolesChoices(models.TextChoices):
        ADMIN = 'ADMIN', _('Admin')
        EDITOR = 'EDITOR', _('Editor')
        VIEWER = 'VIEWER', _('Viewer')
class  Role(models.Model):
      role = models.CharField(max_length=100,choices=RolesChoices.choices,
        default=RolesChoices.VIEWER)
class Roles(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.DO_NOTHING)
    