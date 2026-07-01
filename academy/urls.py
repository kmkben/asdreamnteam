from django.urls import path

from academy import views

app_name = 'academy'

urlpatterns = [
    path('', views.home, name='home'),
    path('categories/', views.categories, name='categories'),
    path('programmes/', views.programs, name='programs'),
    path('horaires/', views.schedules, name='schedules'),
]