from django.test import TestCase
from django.test import Client
import unittest
from django.contrib.auth.models import User


# Create your tests here.
class HomepageTest(TestCase):
    '''tests homepage shows properly'''
    def setUp(self):
        self.client = Client()

    def test_homepage(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)


class GetPhotoTest(unittest.TestCase):
    '''tests get_photo function'''
    def setUp(self):
        self.user = User.objects.create(username='fred', password='password')

    def test_get_photos(self):
        
