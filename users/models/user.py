from django.contrib.auth.models import AbstractUser
from django.contrib.gis.db import models


class User(AbstractUser):

    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    # email = models.EmailField(
    #     verbose_name='email address',
    #     max_length=255,
    #     unique=True,
    # )
    # date_of_birth = models.DateField()
