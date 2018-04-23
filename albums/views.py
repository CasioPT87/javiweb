from django.shortcuts import render
from django.http import HttpResponse
from .models import Photo, Album, PhotoCarrousel

# Create your views here.

def index(request):

    albumsArray = Album.objects.all()

    photoCarrouselArray = PhotoCarrousel.objects.all()

    return render(request, 'albums/index.html', {
        'photosCarrousel': photoCarrouselArray,
        'albums': albumsArray,
        'pageName': 'Home'
    })

def album(request, album):

    albumObj = Album.objects.get(title=album)
    albumId = albumObj.id
    photos = Photo.objects.filter(album=albumId)
    arrayPhotos = []

    albumsArray = Album.objects.all()

    for photo in photos:
        arrayPhotos.append(photo)

    return render(request, 'albums/album.html', {
        'photos': arrayPhotos,
        'albums': albumsArray,
        'pageName': album
    })