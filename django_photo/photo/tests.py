from django.test import TestCase
from django.test import Client


# Create your tests here.
class HomepageTest(TestCase):
    '''tests homepage shows properly'''
    def setUp(self):
        self.client = Client()

    def test_homepage(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
