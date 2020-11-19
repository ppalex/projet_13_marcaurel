
from django.contrib.auth import authenticate
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect, render

from django.views.generic.edit import FormView
from django.views.generic import TemplateView

from .forms import CustomUserCreationForm, CustomUserLoginForm, ContactForm1, ContactForm2

from django.shortcuts import render
from formtools.wizard.views import SessionWizardView


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


class FormWizardView(SessionWizardView):

    template_name = 'users/test.html'

    def done(self, form_list, **kwargs):
        return render(self.request, 'done.html', {
            'form_data': [form.cleaned_data for form in form_list],
        })


class TestFormView(TemplateView):
    template_name = 'users/test2.html'

    def get(self, request, *args, **kwargs):

        user_form = CustomUserCreationForm()
        player_form = CustomUserLoginForm()

        return self.render_to_response(self.get_context_data(user_form=user_form, player_form=player_form))

    def post(self, request, *args, **kwargs):
        user_form = CustomUserCreationForm(
            self.request.POST)
        player_form = CustomUserLoginForm(
            self.request.POST)

        if user_form.is_valid() and player_form.is_valid():
            user_form.save()

            username = user_form.cleaned_data['username']
            password = user_form.cleaned_data['password1']
            authenticate(username=username, password=password)

            return super().form_valid(user_form)
        else:
            return self.form_invalid(user_form, player_form, **kwargs)

    def form_invalid(self, user_form, player_form, **kwargs):
        user_form.prefix = 'user_form'
        player_form.prefix = 'player_form'
        return self.render_to_response(self.get_context_data(user_form=user_form, player_form=player_form))
