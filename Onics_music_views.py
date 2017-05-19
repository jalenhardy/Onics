from django.http import HttpResponse
from django.shortcuts import render
from .models import Album


def index(request):
    albums = Album.objects.all()
    context = {
        "albums": albums
    }
    return render(request, 'music/index.html', context)


def detail(request, album_id):
    return HttpResponse("<h2>Details for Album ID: {} </h2>".format(str(album_id)))

