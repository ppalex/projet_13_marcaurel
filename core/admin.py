from django.contrib import admin

# Register your models here.
from django.contrib.gis.admin import OSMGeoAdmin

from .models.player import Player
from .models.location import Location
from .models.address import Address
from .models.match import Match

@admin.register(Player)
class PlayerAdmin(OSMGeoAdmin):
    list_display = ('name', 'firstname', 'sex', 'level', 'location')


@admin.register(Match)
class MatchAdmin(OSMGeoAdmin):
    list_display = ('classification', 'fixture', 'location')

@admin.register(Location)
class LocationAdmin(OSMGeoAdmin):
    list_display = ('coordinate',)

@admin.register(Address)
class AddressAdmin(OSMGeoAdmin):
    list_display = ('city', 'street', 'number')