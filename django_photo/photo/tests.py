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
