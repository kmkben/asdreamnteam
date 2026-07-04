from django.shortcuts import render

from gallery.models import Album


def albums(request):

    return render(
        request,
        "gallery/albums.html",
        {
            "page": "gallery",
            "albums": Album.objects.filter(
                is_published=True,
            ),
        },
    )