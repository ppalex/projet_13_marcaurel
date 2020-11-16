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
