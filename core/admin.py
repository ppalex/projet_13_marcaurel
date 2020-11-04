from django.contrib import admin

# Register your models here.
from django.contrib.gis.admin import OSMGeoAdmin

from .models.player import Player

admin.site.register(Player)