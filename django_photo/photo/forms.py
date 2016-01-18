from django.forms import ModelForm
from .models import PhotoModel
from django import forms


class PhotoForm(ModelForm):

    class Meta:
        model = PhotoModel
        fields = ['caption', 'photo']


class DeleteForm(forms.Form):
    photo_id = forms.HiddenInput()
    orig = forms.HiddenInput()
    temp = forms.HiddenInput()
