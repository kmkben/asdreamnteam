from django.shortcuts import render

from team.models import ClubMember


def members(request):
    members = ClubMember.objects.filter(is_active=True)

    return render(request, "team/members.html", {
        "page": "members",
        "members": members,
    })