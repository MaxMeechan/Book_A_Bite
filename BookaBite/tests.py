from django.test import TestCase, Client
from django.urls import reverse, resolve
from django.contrib.auth.models import User
from BookaBite.models import UserProfile, Menu, Item, Bookings, Reviews
from BookaBite.forms import UserForm, UserProfileForm
from BookaBite import views
from population_script import populate
from datetime import date, time

class BaseTestCase(TestCase):
    def setUp(self):
        populate()
        self.client = Client()

#Model
class ModelTests(BaseTestCase):

    def test_user_profile_created(self):
        profile = UserProfile.objects.first()
        self.assertIsNotNone(profile)
        self.assertEqual(profile.Username, "Chef John")

    def test_menu_and_item(self):
        menu = Menu.objects.first()
        self.assertIsNotNone(menu)
        item = Item.objects.filter(MenuName=menu).first()
        self.assertIsNotNone(item)
        self.assertEqual(item.MenuName, menu)

    def test_booking_exists(self):
        booking = Bookings.objects.first()
        self.assertIsNotNone(booking)
        self.assertEqual(booking.partyMembers, 2)

    def test_review_exists(self):
        review = Reviews.objects.first()
        self.assertIsNotNone(review)
        self.assertEqual(review.RatingNum, 5)

#Forms
class FormTests(BaseTestCase):

    def test_user_form_valid(self):
        form = UserForm(data={
            'username': 'formtest',
            'email': 'form@test.com',
            'password': 'formpass123'
        })
        self.assertTrue(form.is_valid())

    def test_user_profile_form_valid(self):
        form = UserProfileForm(data={
            'Username': 'formtest',
            'firstName': 'Form',
            'surname': 'Tester',
            'email': 'form@test.com',
            'Password': 'formpass123'
        })
        self.assertTrue(form.is_valid())

#Views
class ViewTests(BaseTestCase):

    def test_home_view_status(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_menu_view_status(self):
        response = self.client.get(reverse('BookaBite:menu'))
        self.assertEqual(response.status_code, 200)

    def test_login_view_status(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)

#URLs
class URLTests(BaseTestCase):

    def test_home_url_resolves(self):
        resolver = resolve('/')
        self.assertEqual(resolver.func, views.home)

    def test_menu_url_resolves(self):
        resolver = resolve('/BookaBite/menu/')
        self.assertEqual(resolver.func, views.menu)

    def test_login_url_resolves(self):
        resolver = resolve('/login/')
        self.assertEqual(resolver.func, views.user_login)
