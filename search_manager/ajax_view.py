from django.http import JsonResponse

from core.models.address import Address
from core.models.match import Match

from core.models.player import Player
from .utils import km_to_degrees

from django.contrib.auth.decorators import login_required


@login_required
def filter_match_view(request, *args, **kwargs):

    context = {
        'object_list': []
    }
    if request.POST:

        if (request.POST.get('classification') != ''):
            key = '{0}__{1}'.format('classification', 'exact')
            value = request.POST.get('classification')
            kwargs[key] = value

        if (request.POST.get('city')) != '':
            key = '{0}__{1}__{2}'.format('address', 'city', 'exact')
            value = request.POST.get('city')
            kwargs[key] = value

        if (request.POST.get('available_place') != ''):
            key = '{0}__{1}'.format('available_place', 'exact')
            value = request.POST.get('available_place')
            kwargs[key] = value

        if (request.POST.get('start_fixture') != ''):
            key = '{0}__{1}'.format('start_fixture', 'contains')
            value = request.POST.get('start_fixture')
            kwargs[key] = value

        if (request.POST.get('location') != ''):

            player_location = request.user.player.location
            distance_km = request.POST.get('location')
            distance_degrees = km_to_degrees(int(distance_km))

            key = '{0}__{1}__{2}'.format('location', 'coordinates', 'dwithin')
            value = (player_location.coordinates, distance_degrees)
            kwargs[key] = value

        qs = Match.objects.filter(**kwargs)

        for match in qs:

            match_dict = {
                'id': match.id,
                'classification': match.classification,
                'lat_lng': match.location.lat_lng
            }

            context['object_list'].append(match_dict)

    return JsonResponse(context['object_list'], safe=False)


@login_required
def filter_player_view(request, *args, **kwargs):

    context = {
        'object_list': []
    }
    if (request.POST.get('location') != ''):

        player_location = request.user.player.location
        distance_km = request.POST.get('location')
        distance_degrees = km_to_degrees(int(distance_km))

        key = '{0}__{1}__{2}'.format('location', 'coordinates', 'dwithin')
        value = (player_location.coordinates, distance_degrees)
        kwargs[key] = value

    qs = Player.objects.filter(**kwargs)
    qs = qs.exclude(pk=request.user.id)

    for player in qs:

        player_dict = {
            'id': player.id,
            'username': player.user.username,
            'lat_lng': player.location.lat_lng
        }

        context['object_list'].append(player_dict)

    return JsonResponse(context['object_list'], safe=False)


@login_required
def autocomplete_city(request):
    """This function is used to autocomplete search bar with products
    from database.

    Args:
        request ([HttpRequest]): Contains the metadata about the request.

    Returns:
        [ HttpResponse]: Contains the response for the home page view.
    """

    if 'term' in request.GET:
        query = Address.objects.filter(
            city__istartswith=request.GET.get('term'))
        addresses = list()

        for address in query:
            addresses.append(address.city)

        return JsonResponse(addresses, safe=False)

    return None


@login_required
def autocomplete_player(request):
    """This function is used to autocomplete search bar with products
    from database.

    Args:
        request ([HttpRequest]): Contains the metadata about the request.

    Returns:
        [ HttpResponse]: Contains the response for the home page view.
    """

    if 'term' in request.GET:

        query = Player.objects.get_player_name_start_with(
            request.GET.get('term'))

        players = list()

        for player in query:
            players.append(player.user.username)

        return JsonResponse(players, safe=False)

    return None


@login_required
def get_user_current_coordinates(request):

    latitude = request.POST.get('latitude')
    longitude = request.POST.get('longitude')
    player = request.user.player
    player.update_location(latitude, longitude)

    return JsonResponse({'status': 200})
