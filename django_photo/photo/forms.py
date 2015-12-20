from django.forms import ModelForm
from .models import PhotoModel


class PhotoForm(ModelForm):

    class Meta:
        model = PhotoModel
        fields = ['caption', 'photo']
