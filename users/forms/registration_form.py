from django.contrib.auth.forms import UserCreationForm
from users.models.user import User

from django import forms


class CustomUserCreationForm(UserCreationForm):
    """This class represents the user register form.
    """

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control form-control-user',
                'type': 'text',
                'placeholder': "Nom d'utilisateur"}),

            'email': forms.TextInput(attrs={
                'class': 'form-control form-control-user',
                'type': 'text',
                'placeholder': "Adresse mail"}),

        }

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget = forms.PasswordInput(attrs={
            'class': 'form-control form-control-user',
            'placeholder': "Mot de passe"})

        self.fields['password2'].widget = forms.PasswordInput(attrs={
            'class': 'form-control form-control-user',
            'placeholder': "Confirmer le mot de passe"})

    def clean_username(self):
        username = self.cleaned_data.get("username")
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Le nom d'utilisateur existe déjà")
        return username

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("L'emai existe déjà")
        return email
