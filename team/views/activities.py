from django.shortcuts import render


def activities(request):
    return render(
        request,
        "team/activities.html",
        {
            "page": "activities",
        },
    )