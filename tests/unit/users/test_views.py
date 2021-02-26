from django.test import TestCase
from django.urls import reverse
from users.models.user import User


class RegisterViewTest(TestCase):

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/register/')

        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('register'))

        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('register'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/register.html')


class CustomLoginViewTest(TestCase):

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/login/')

        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('login'))

        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('login'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/login.html')


class CustomLogoutViewTest(TestCase):
    fixtures = ["data.json"]

    def setUp(self):
        for user in User.objects.all():
            user.set_password(user.password)
            user.save()

    def test_view_url_exists_at_desired_location(self):
        self.client.login(
            username='user1', password='user1')
        response = self.client.get('logout/')

        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        self.client.login(
            username='user1', password='user1')
        response = self.client.get(reverse('logout'))

        self.assertEqual(response.status_code, 302)


class UserSettingsViewTest(TestCase):

    fixtures = ["data.json"]

    def setUp(self):
        for user in User.objects.all():
            user.set_password(user.password)
            user.save()

    def test_view_url_exists_at_desired_location(self):
        self.client.login(
            username='user1', password='user1')
        response = self.client.get('settings/profile/')

        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        self.client.login(
            username='user1', password='user1')
        response = self.client.get(reverse('settings-profile'))

        self.assertEqual(response.status_code, 200)


class ProfileViewTest(TestCase):

    fixtures = ["data.json"]

    def setUp(self):
        for user in User.objects.all():
            user.set_password(user.password)
            user.save()

    def test_view_url_exists_at_desired_location(self):
        self.client.login(
            username='user1', password='user1')
        response = self.client.get('profile/user1')

        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        self.client.login(
            username='user1', password='user1')
        response = self.client.get(
            reverse('profile', kwargs={'username': "user1"}))

        self.assertEqual(response.status_code, 200)
