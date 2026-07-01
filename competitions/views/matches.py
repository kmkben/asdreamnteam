from django.shortcuts import render

from competitions.models import Match


def matches(request):
    matches_list = Match.objects.select_related("competition").all()

    return render(request, "competitions/matches.html", {
        "page": "competitions",
        "matches": matches_list,
    })