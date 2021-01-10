from django.test import TestCase

from users.forms.login_form import CustomUserLoginForm
from users.forms.registration_form import CustomUserCreationForm


class CustomUserCreationFormTest(TestCase):
    def test_form(self):

        data = {
            'username': 'testuser',
            'email': 'testuser@gmail.com',
            'password1': 'Alsjdsd52&',
            'password2': 'Alsjdsd52&',
        }

        form = CustomUserCreationForm(data)

        self.assertTrue(form.is_valid())

    def test_clean_username(self):
        data = {
            'username': 'testuser1',
            'email': 'testuser1@gmail.com',
            'password1': 'Alsjdsd52&',
            'password2': 'Alsjdsd52&',
        }

        form = CustomUserCreationForm(data)
        if form.is_valid():
            username = form.cleaned_data.get("username")

        self.assertEqual(username, 'testuser1')

    def test_clean_email(self):
        data = {
            'username': 'testuser1',
            'email': 'testuser1@gmail.com',
            'password1': 'Alsjdsd52&',
            'password2': 'Alsjdsd52&',
        }

        form = CustomUserCreationForm(data)
        if form.is_valid():
            email = form.cleaned_data.get("email")

        self.assertEqual(email, 'testuser1@gmail.com')


# class CustomUserLoginFormTest(TestCase):
#     fixtures = ["data.json"]

#     def test_form(self):

#         data = {
#             'username': 'user1',
#             'password': 'user1',
#         }

#         form = CustomUserLoginForm(None, data=data)

#         print(form.error_messages)

#         self.assertTrue(form.is_valid())
