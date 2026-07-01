from django.urls import path

from competitions import views

app_name = 'competitions'

urlpatterns = [
    path('', views.home, name='home'),
    path('competitions/', views.competitions, name='competitions'),
    path('matches/', views.matches, name='matches'),
]