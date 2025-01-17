
from django import forms
from django.contrib.auth.forms import AuthenticationForm


class CustomUserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control form-control-user',
        'type': 'text',
                'placeholder': "Nom d'utilisateur"}))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control form-control-user',
        'placeholder': "Mot de passe"}))
