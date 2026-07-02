from django.urls import path

from news import views

app_name = 'news'

urlpatterns = [

    path(
        '',
        views.home,
        name='home',
    ),

    path(
        'articles/',
        views.articles,
        name='articles',
    ),

    path(
        '<slug:slug>/',
        views.article,
        name='article',
    ),

]