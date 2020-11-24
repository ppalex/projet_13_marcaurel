from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from django.views import generic
from django.contrib.gis.geos import fromstr, Point
from django.contrib.gis.db.models.functions import Distance


@login_required
def index(request):
    """This function displays the home page views.

    Args:
        request ([HttpRequest]): Contains the metadata about the request.

    Returns:
        [ HttpResponse]: Contains the response for the home page view.
    """

    return render(request, 'core/base.html')
