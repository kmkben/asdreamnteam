from django.shortcuts import render

from gallery.models import Album


def home(request):

    featured = Album.objects.filter(
        featured=True,
        is_published=True,
    ).first()

    albums = Album.objects.filter(
        is_published=True,
    )[:6]
    
    context = {
            "page": "gallery",
            "featured": featured,
            "albums": albums,
        }

    return render(request, "gallery/home.html", context)