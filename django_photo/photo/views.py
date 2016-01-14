from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from .forms import PhotoForm
from .models import PhotoModel


# Mixins
class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view)


# functions
def get_photos(user):
    '''returns all photos of a user'''

    photos = PhotoModel.objects.filter(owner=user)
    return photos


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
        # get the 
        social_user = request.user.social_auth.filter(provider='facebook').first()

        # check if any photo is to be editted
        staged_photo = None
        if 'photo' in request.GET:
            # get object of the photo to be editted
            staged_photo = PhotoModel.objects.get(id=request.GET['photo'])

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
