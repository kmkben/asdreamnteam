from django.urls import path

from gallery import views

app_name = 'gallery'

urlpatterns = [

    path(
        '',
        views.home,
        name='home',
    ),

    path(
        'albums/',
        views.albums,
        name='albums',
    ),

    path(
        'album/<slug:slug>/',
        views.album,
        name='album',
    ),

]