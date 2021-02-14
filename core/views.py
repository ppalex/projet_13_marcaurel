from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.utils import timezone


def landing(request):

    template_name = 'core/landing.html'
    return render(request, template_name)


def legal(request):
    context = {
        'timezone': timezone.now()
    }
    template_name = 'core/legal.html'
    return render(request, template_name, context=context)


class Index(LoginRequiredMixin, TemplateView):
    template_name = 'core/base.html'


def custom_page_not_found_view(request, exception):
    return render(request, "core/404.html", {})
