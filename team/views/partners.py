from django.shortcuts import render

from team.models import Partner


def partners(request):
    partners_list = Partner.objects.filter(
        is_active=True
    )

    return render(
        request,
        "team/partners.html",
        {
            "page": "partners",
            "partners": partners_list,
        },
    )