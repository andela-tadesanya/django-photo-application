from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from .forms import PhotoForm
from .models import PhotoModel
from PIL import Image
import os
import shutil
from .effects import double, nigeria, france, usa, kenya, russia


# Mixins
class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view)


# helper functions
def get_photos(user):
    '''returns all photos of a user'''

    photos = PhotoModel.objects.filter(owner=user)
    return photos


def create_duplicate_file(image_file_path, image_file_url):
    '''creates a duplicate file for editting'''
    # create temporary file path
    root, ext = os.path.splitext(image_file_path)
    root = root + '_temp'
    temp_file_path = root + ext

    # create temporary file url
    root, ext = os.path.splitext(image_file_url)
    root = root + '_temp'
    temp_file_url = root + ext

    # create a duplicate of the image file
    shutil.copy2(image_file_path, temp_file_path)

    # return the new file path
    return temp_file_path, temp_file_url


def photo_effect(effect, temp_file_path, temp_file_url):
    '''applies a photo effect on a temporary file'''
    if effect == 'double':
        double(temp_file_path)
        return temp_file_url
    elif effect == 'france':
        france(temp_file_path)
        return temp_file_url
    elif effect == 'kenya':
        kenya(temp_file_path)
        return temp_file_url
    elif effect == 'nigeria':
        nigeria(temp_file_path)
        return temp_file_url
    elif effect == 'russia':
        russia(temp_file_path)
        return temp_file_url
    elif effect == 'usa':
        usa(temp_file_path)
        return temp_file_url
    else:
        return None


# Views
class HomePageView(View):
    '''handles homepage requests'''
    template_name = 'photo/index.html'

    def get(self, request):
        # redirect to user dashboard if user is logged in
        if request.user and not request.user.is_anonymous:
            return HttpResponseRedirect(reverse('photo:user_home'))
        else:
            return render(request, self.template_name)


class DashboardView(LoginRequiredMixin, View):
    '''displays dashboard'''
    template_name = 'photo/dashboard.html'

    def get(self, request):
        # get the user's social details
        social_user = request.user.social_auth.filter(provider='facebook').first()

        # check if any photo is to be editted
        staged_photo = None
        if 'photo' in request.GET:
            # get object of the photo to be editted
            staged_photo = PhotoModel.objects.get(id=request.GET['photo'])


            # set original image as image to be displayed
            staged_photo.display_image = staged_photo.photo.url

        # check if any effect are to be applied
        if 'effect' in request.GET:
            # create a temporary image to use for editting
            staged_photo.temp_file_path, staged_photo.temp_file_url = create_duplicate_file(staged_photo.photo.path, staged_photo.photo.url)
            staged_photo.temp_file_url = photo_effect(request.GET['effect'], staged_photo.temp_file_path, staged_photo.temp_file_url)

            # set temporary image as image to be displayed
            staged_photo.display_image = staged_photo.temp_file_url

        # get user's photos
        photos = get_photos(request.user)
        context = {'social_user': social_user,
                   'photos': photos,
                   'staged_photo': staged_photo}
        return render(request, self.template_name, context)


class ImageUploadView(LoginRequiredMixin, View):
    '''handles image upload'''

    def post(self, request):
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            # set the current user as the owner of the photo before
            # saving the photo
            photo = form.save(commit=False)
            photo.owner = request.user
            photo.save()
            return HttpResponseRedirect(reverse('photo:user_home'))
        else:
            return HttpResponseRedirect(reverse('photo:user_home'))
