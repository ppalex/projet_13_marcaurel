
from django.contrib.auth import authenticate
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormView

from .forms.registration_form import CustomUserCreationForm
from .forms.login_form import CustomUserLoginForm


from django.views.generic.edit import CreateView
from django.http import Http404
from django.shortcuts import render
from django.views.generic import View

from core.models.player import Player

from .forms.profile_form import PlayerCreateForm, AddressCreateForm


class RegisterView(FormView):
    template_name = 'users/register.html'
    form_class = CustomUserCreationForm
    success_url = '/index/'

    def form_valid(self, form):

        form.save()

        username = form.cleaned_data['username']
        password = form.cleaned_data['password1']
        authenticate(username=username, password=password)

        return super().form_valid(form)


class CustomLoginView(SuccessMessageMixin, LoginView):
    """This class displays the login view.
    """
    success_url = 'index'
    template_name = 'users/login.html'
    form_class = CustomUserLoginForm
    success_message = "Vous êtes connectés %(username)s"


class CustomLogoutView(SuccessMessageMixin, LogoutView):
    """This class is used to logout the user.
    """
    success_url = 'login/'
    success_message = "Vous êtes déconnectés"


# class CreatePlayerView(CreateView):
#     form_class = PlayerCreateForm
#     model = Player

#     template_name = 'player/player_creation.html'


class CreatePlayerView(View):
    template_name = 'users/profile.html'

    def get_context_data(self,  **kwargs):
        if 'player_form' not in kwargs:
            kwargs['player_form'] = PlayerCreateForm()
        if 'address_form' not in kwargs:
            kwargs['address_form'] = AddressCreateForm()

        return kwargs

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_context_data())

    def post(self, request, *args, **kwargs):

        context = {}

        player_form = PlayerCreateForm(request.POST)
        address_form = AddressCreateForm(request.POST)
        print(player_form.errors)
        print(address_form.is_valid())
        if player_form.is_valid() and address_form.is_valid():

            pass

        else:
            print('nok')
            context['player_form'] = player_form
            context['address_form'] = address_form

            return render(request, self.template_name, context)


class UserSettings(View, LoginRequiredMixin):
    template_name = 'users/settings.html'

    def get_context_data(self,  **kwargs):
        if 'player_form' not in kwargs:
            kwargs['player_form'] = PlayerCreateForm(
                instance=self.request.user.profile)

        if 'address_form' not in kwargs:
            kwargs['address_form'] = AddressCreateForm(
                instance=self.request.user.profile)

        return kwargs

    def get(self, request, *args, **kwargs):

        return render(request, self.template_name, self.get_context_data())

    def post(self, request, *args, **kwargs):

        context = {}

        player_form = PlayerCreateForm(request.POST)
        address_form = AddressCreateForm(request.POST)
        if player_form.is_valid() and address_form.is_valid():
            pass

        else:
            context['player_form'] = player_form
            context['address_form'] = address_form

            return render(request, self.template_name, context)
