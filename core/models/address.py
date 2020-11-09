from django.db import models


class Address(models.Model):
    city = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    number = models.IntegerField()
    region = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "Addresses"
