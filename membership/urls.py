from django.urls import path

from membership import views

app_name = "membership"

urlpatterns = [
    path("", views.home, name="home"),
]