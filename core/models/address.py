from django.db import models


class Address(models.Model):
    city = models.CharField(max_length=255, null=True, blank=True)
    street = models.CharField(max_length=255, null=True, blank=True)
    number = models.IntegerField(blank=True, null=True)
    region = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Addresses"
