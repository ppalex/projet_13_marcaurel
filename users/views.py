
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect, reverse
from django.views.generic import View, DetailView, UpdateView
from .models.user import User
from core.models.address import Address

from api_manager.utils.mapquest_utils import get_address_coordinates
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
        context['age'] = player.user.profile.get_age()

        return context


class UserSettingsView(UpdateView, LoginRequiredMixin):
    template_name = 'users/settings.html'
    model = User

    def get_object(self):
        user = get_object_or_404(User, id=self.request.user.id)
        return user.player

    def form_invalid(self, request, **kwargs):
        return render(request, self.template_name, self.get_context_data(**kwargs))

    def get_context_data(self,  **kwargs):

        if 'player_form' not in kwargs:
            kwargs['player_form'] = ProfileCreateForm(
                instance=self.request.user.profile)

        if 'address_form' not in kwargs:
            kwargs['address_form'] = AddressCreateForm(
                instance=self.request.user.profile.address)

        return kwargs

    def post(self, request, *args, **kwargs):
        player = self.get_object()

        player_form = ProfileCreateForm(
            request.POST, instance=player.user.profile)
        address_form = AddressCreateForm(
            request.POST, instance=player.user.profile.address)

        if player_form.is_valid() and address_form.is_valid():
            profile = request.user.profile

            city = address_form.cleaned_data['city']
            street = address_form.cleaned_data['street']
            number = address_form.cleaned_data['number']
            region = address_form.cleaned_data['region']

            latitude, longitude = get_address_coordinates(
                street, number, city, region)

            player.update_location(latitude, longitude)

            player = player_form.save(commit=False)

            if profile.address is None:
                address = Address.objects.create(
                    city=city,
                    street=street,
                    number=number,
                    region=region
                )

            else:
                address = address_form.save()

            player.address = address
            player.save()
            player_form.save_m2m()
            messages.success(request, "Votre profil a été mis à jour!")

            return redirect(reverse('settings-profile'))

        else:
            return self.form_invalid(request, **{'player_form': player_form,
                                                 'address_form': address_form})
