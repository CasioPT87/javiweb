# Create your models here.

from django.db import models

class Album(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['title']

class Photo(models.Model):
    name = models.CharField(max_length=30)
    album = models.ForeignKey(Album, on_delete=False)
    image = models.ImageField(null=True, blank=True, upload_to='photos', height_field=None, width_field=None, max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

class PhotoCarrousel(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField(null=True, blank=True, upload_to='photosCarrousel', height_field=None, width_field=None, max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

    