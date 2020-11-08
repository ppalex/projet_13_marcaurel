from django.contrib import admin

# Register your models here.
from django.contrib.gis.admin import OSMGeoAdmin

from .models.player import Player
from .models.location import Location
from .models.address import Address
from .models.match import Match
from .models.invitation import Invitation
from .models.registration import Registration

@admin.register(Player)
class PlayerAdmin(OSMGeoAdmin):
    list_display = ('id' , 'name', 'firstname', 'sex', 'level', 'location')


@admin.register(Match)
class MatchAdmin(OSMGeoAdmin):
    list_display = ('classification', 'fixture', 'location', 'administrator')

@admin.register(Location)
class LocationAdmin(OSMGeoAdmin):
    list_display = ('coordinate',)

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('city', 'street', 'number')


@admin.register(Invitation)
class InvitationAdmin(admin.ModelAdmin):
    list_display = ('id', 'status', 'invitation_date', 'response_date', 'for_player', 'by_player', 'for_match')


@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('id', 'join_date', 'invitation')