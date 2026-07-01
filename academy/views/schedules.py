from django.shortcuts import render

from academy.models import TrainingSchedule


def schedules(request):
    schedules = TrainingSchedule.objects.filter(is_active=True).select_related("category")

    return render(request, "academy/schedules.html", {
        "page": "academy",
        "schedules": schedules,
    })