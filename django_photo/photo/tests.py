from django.test import TestCase, Client
from django.contrib.auth.models import User
from .views import create_duplicate_file, get_photos, photo_effect
from .models import PhotoModel
from PIL import Image
import os
import unittest


class URLTest(unittest.TestCase):
    '''tests URLs'''

    def setUp(self):
        self.client = Client()

    def test_landing_page(self):
        '''tests the landing page'''
        user = User.objects.create_user(username='myuser', password='mypass')
        user.save()
        self.client.login(username='myuser', password='mypass')
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_dashboard(self):
        user = User.objects.create_user(username='auser', password='mypass')
        user.save()
        self.client.login(username='auser', password='mypass')
        response = self.client.get('/user/')
        self.assertEqual(response.status_code, 200)


class FunctionTest(TestCase):
    '''tests homepage shows properly'''

    @classmethod
    def setUpClass(cls):
        cls.image = Image.new('RGBA', size=(500, 500))
        cls.image.save('test.jpg')
        cls.image_path = os.path.abspath('test.jpg')

    @classmethod
    def tearDownClass(cls):
        os.remove('test.jpg')
        os.remove('test_temp.jpg')

    def test_call_to_get_photo(self):
        user = User.objects.create(username='auser', password='mypass')
        PhotoModel.objects.create(caption='My photo', owner=user)
        photos = get_photos(user)
        self.assertTrue(photos[0].caption, 'My photo')

    def test_file_duplication(self):
        path, url = create_duplicate_file(self.image_path, self.image_path)
        self.assertIn('_temp', path)
        self.assertIn('_temp', url)

    def test_effect_double(self):
        path, url = create_duplicate_file(self.image_path, self.image_path)
        response = photo_effect('double', path, url)
        self.assertEqual(url, response)

    def test_effect_france(self):
        path, url = create_duplicate_file(self.image_path, self.image_path)
        response = photo_effect('france', path, url)
        self.assertEqual(url, response)

    def test_effect_kenya(self):
        path, url = create_duplicate_file(self.image_path, self.image_path)
        response = photo_effect('kenya', path, url)
        self.assertEqual(url, response)

    def test_effect_nigeria(self):
        path, url = create_duplicate_file(self.image_path, self.image_path)
        response = photo_effect('nigeria', path, url)
        self.assertEqual(url, response)

    def test_effect_russia(self):
        path, url = create_duplicate_file(self.image_path, self.image_path)
        response = photo_effect('russia', path, url)
        self.assertEqual(url, response)

    def test_effect_usa(self):
        path, url = create_duplicate_file(self.image_path, self.image_path)
        response = photo_effect('usa', path, url)
        self.assertEqual(url, response)

    def test_effect_none(self):
        path, url = create_duplicate_file(self.image_path, self.image_path)
        response = photo_effect('', path, url)
        self.assertEqual(None, response)
