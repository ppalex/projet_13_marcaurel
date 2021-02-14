
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from django.views.generic import View, DetailView
from django.views import View
from .models.user import User
from core.models.address import Address

from .forms.login_form import CustomUserLoginForm
from .forms.profile_form import AddressCreateForm, ProfileCreateForm
from .forms.registration_form import CustomUserCreationForm
from django.shortcuts import get_object_or_404
from django.contrib import messages


class RegisterView(View):
    template_name = 'users/register.html'
    custom_form = CustomUserCreationForm

    def get(self, request):
        form = self.custom_form()
        context = {'form': form}

        return render(request, self.template_name, context)

    def post(self, request):
        form = self.custom_form(request.POST)
        context = {'form': form}

        if form.is_valid():

            form.save()

            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "Bienvenue, votre compte a été créé!")

            return redirect('index')

        return render(request, self.template_name, context)


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


class ProfileView(DetailView, LoginRequiredMixin):

    model = User
    template_name = "users/profile.html"

    def get_object(self):

        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return user.player

    def get_context_data(self, **kwargs):

        context = super(ProfileView, self).get_context_data(**kwargs)

        player = self.get_object()

        context['followers_count'] = player.get_followers_count()
        context['followings_count'] = player.get_followings_count()

        return context


class UserSettingsView(View, LoginRequiredMixin):
    template_name = 'users/settings.html'

    def get_context_data(self,  **kwargs):
        if 'player_form' not in kwargs:
            kwargs['player_form'] = ProfileCreateForm(
                instance=self.request.user.profile)

        if 'address_form' not in kwargs:
            kwargs['address_form'] = AddressCreateForm(
                instance=self.request.user.profile.address)

        return kwargs

    def get(self, request, *args, **kwargs):

        return render(request, self.template_name, self.get_context_data())

    def post(self, request, *args, **kwargs):

        player_form = ProfileCreateForm(request.POST)
        address_form = AddressCreateForm(request.POST)

        if player_form.is_valid() and address_form.is_valid():
            profile = request.user.profile

            city = address_form.cleaned_data['city']
            street = address_form.cleaned_data['street']
            number = address_form.cleaned_data['number']
            region = address_form.cleaned_data['region']

            address = Address.objects.create(
                city=city,
                street=street,
                number=number,
                region=region
            )

            address.save()

            profile.firstname = player_form.cleaned_data['firstname']
            profile.name = player_form.cleaned_data['name']
            profile.birthdate = player_form.cleaned_data['birthdate']
            profile.sex = player_form.cleaned_data['sex']
            profile.level = player_form.cleaned_data['level']
            positions = player_form.cleaned_data['positions']
            profile.address = address

            profile.positions.add(*positions)
            profile.save()

            return render(request, self.template_name, self.get_context_data())

        else:

            return render(request, self.template_name, self.get_context_data())
