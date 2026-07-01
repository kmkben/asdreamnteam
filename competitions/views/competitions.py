from django.shortcuts import render

from competitions.models import Competition


def competitions(request):
    competitions_list = Competition.objects.filter(is_active=True).order_by("order")

    return render(request, "competitions/competitions.html", {
        "page": "competitions",
        "competitions": competitions_list,
    })