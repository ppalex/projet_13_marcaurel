from django.contrib import admin

# Register your models here.
from django.contrib.gis.admin import OSMGeoAdmin

from .models.player import Player
from .models.location import Location
from .models.address import Address
from .models.match import Match
from .models.invitation import Invitation
from .models.registration import Registration
from .models.position import Position
from .models.match_request import MatchRequest


@admin.register(Player)
class PlayerAdmin(OSMGeoAdmin):
    list_display = ('id', 'name', 'firstname', 'sex', 'level', 'location')


@admin.register(Match)
class MatchAdmin(OSMGeoAdmin):
    list_display = ('classification', 'fixture', 'location', 'administrator')


@admin.register(Location)
class LocationAdmin(OSMGeoAdmin):

    default_lon = 04.40
    default_lat = 50.38

    list_display = ('coordinates',)


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('city', 'street', 'number')


@admin.register(Invitation)
class InvitationAdmin(admin.ModelAdmin):
    list_display = ('id', 'status', 'invitation_date',
                    'response_date', 'for_player', 'by_player', 'for_match')


@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('id', 'join_date', 'invitation')


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ('position_name',)


@admin.register(MatchRequest)
class MatchRequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'status', 'request_date',
                    'response_date', 'by_player', 'for_match')
