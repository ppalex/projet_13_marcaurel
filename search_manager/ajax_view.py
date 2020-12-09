from django.http import JsonResponse, HttpResponse
from core.models.match import Match
from core.models.address import Address
import pdb

def filter_match_view(request, *args, **kwargs):

    context = {
        'object_list': []
    }

    if (request.POST.get('classification')) != '':
        key = '{0}__{1}'.format('classification', 'exact')
        value = request.POST.get('classification')
        kwargs[key] = value

    if (request.POST.get('city')) != '':
        key = '{0}__{1}__{2}'.format('address', 'city', 'exact')
        value = request.POST.get('city')
        kwargs[key] = value

    if (request.POST.get('available_place')) != '':
        key = '{0}__{1}'.format('available_place', 'exact')
        value = request.POST.get('available_place')
        kwargs[key] = value

    if (request.POST.get('fixture')) != '':
        key = '{0}__{1}'.format('fixture', 'contains')
        value = request.POST.get('fixture')
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


def get_user_current_coordinates(request):

    latitude = request.POST.get('latitude')
    longitude = request.POST.get('longitude')
    player = request.user.player
    player.update_location(latitude, longitude)
    
    return JsonResponse({'status': 200})
