from django.shortcuts import render

from team.models import ClubMember, Partner, Sponsor


def presentation(request):
    staff_members = ClubMember.objects.filter(
        is_active=True
    ).exclude(
        role=ClubMember.Role.PLAYER
    )[:6]

    sponsors = Sponsor.objects.filter(is_active=True)[:6]
    partners = Partner.objects.filter(is_active=True)[:6]

    return render(request, "team/presentation.html", {
        "page": "presentation",
        "staff_members": staff_members,
        "sponsors": sponsors,
        "partners": partners,
    })