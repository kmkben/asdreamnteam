from django.urls import path

from donation import views

app_name = "donation"

urlpatterns = [

    path(
        "",
        views.donation,
        name="donation",
    ),

]