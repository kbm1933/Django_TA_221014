import imp
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.

class UserModel(AbstractBaseUser):
    class Meta:
        db_table = 'my_user'
    phone = models.TextField(_MAX_LENGTH=50,blank=True)
    address = models.TextField(_MAX_LENGTH=256,blank=True)
    