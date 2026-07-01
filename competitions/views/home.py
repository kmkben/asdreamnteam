from django.shortcuts import render

from competitions.models import Competition, Match


def home(request):
    competitions = Competition.objects.filter(is_active=True).order_by("order")[:4]
    upcoming_matches = Match.objects.filter(status=Match.Status.UPCOMING).select_related("competition")[:4]
    latest_results = Match.objects.filter(status=Match.Status.FINISHED).select_related("competition")[:4]

    return render(request, "competitions/home.html", {
        "page": "competitions",
        "competitions": competitions,
        "upcoming_matches": upcoming_matches,
        "latest_results": latest_results,
    })