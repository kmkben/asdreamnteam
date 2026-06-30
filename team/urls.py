from django.urls import path

from . import views

app_name = 'team'

urlpatterns = [
    path(
        'presentation/',
        views.presentation,
        name='presentation',
    ),

    path(
        'members/',
        views.members,
        name='members',
    ),

    path(
        'activities/',
        views.activities,
        name='activities',
    ),

    path(
        'sponsors/',
        views.sponsors,
        name='sponsors',
    ),

    path(
        'partners/',
        views.partners,
        name='partners',
    ),
]