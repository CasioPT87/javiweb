from django.shortcuts import render
from django.http import HttpResponse
from .models import Photo, Album, PhotoCarrousel, Headboard

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
    headboards = Headboard.objects.filter(album=albumId)
    headboardsArray = []

    albumsArray = Album.objects.all()

    for photo in photos:
        arrayPhotos.append(photo)

    for headboard in headboards:
        headboardsArray.append(headboard)

    return render(request, 'albums/album.html', {
        'photos': arrayPhotos,
        'albums': albumsArray,
        'pageName': album,
        'headboard': headboardsArray[0]
    })