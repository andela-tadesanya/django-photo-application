from __future__ import unicode_literals

from django.db import models


# Create your models here.
class PhotoModel(models.Model):
    caption = models.CharField('Caption',
                               max_length=100,
                               blank=False)
    photo = models.ImageField('Your Photos',
                              upload_to='photos/%Y/%m/%d',
                              default='photos/none/default.jpg')
    date_created = models.DateTimeField('Created on',
                                        null=True,
                                        blank=True,
                                        auto_now_add=True)
