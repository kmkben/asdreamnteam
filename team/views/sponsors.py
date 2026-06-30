from django.shortcuts import render

from team.models import Sponsor, Partner


def sponsors(request):
    sponsors_list = Sponsor.objects.filter(is_active=True)
    partners = Partner.objects.filter(is_active=True)

    return render(request, "team/sponsors.html", {
        "page": "sponsors",
        "sponsors": sponsors_list,
        "partners": partners,
    })