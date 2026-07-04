from django.shortcuts import get_object_or_404
from django.shortcuts import render

from gallery.models import Album


def album(request, slug):

    album = get_object_or_404(
        Album,
        slug=slug,
        is_published=True,
    )

    return render(
        request,
        "gallery/album.html",
        {
            "page": "gallery",
            "album": album,
            "photos": album.photos.all(),
        },
    )