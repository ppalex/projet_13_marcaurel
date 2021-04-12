from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import TemplateView


def landing(request):
    """ This method displays the landing page view.
    """
    template_name = 'core/landing.html'

    return render(request, template_name)


def legal(request):
    """ This method displays the legal page view.
    """
    template_name = 'core/legal.html'

    return render(request, template_name)


class Index(LoginRequiredMixin, TemplateView):
    """ This method displays the index page view.
    """
    template_name = 'core/base.html'


def custom_page_not_found_view(request, exception):
    """ This method displays the a 404 page view.
    """
    return render(request, "core/404.html", {})
