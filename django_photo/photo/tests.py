from django.test import TestCase, Client, RequestFactory
from django.contrib.auth.models import User
import mock
from .views import create_duplicate_file, get_photos
from .models import PhotoModel
from io import BytesIO
from PIL import Image
import os


class HomepageTest(TestCase):
    '''tests homepage shows properly'''

    @classmethod
    def setUpClass(cls):
        cls.client = Client()
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
