from django.shortcuts import render

from academy.models import TrainingCategory, TrainingProgram, TrainingSchedule


def home(request):
    categories = TrainingCategory.objects.filter(is_active=True).order_by("order")[:4]
    programs = TrainingProgram.objects.filter(is_active=True).select_related("category").order_by("order")[:4]
    schedules = TrainingSchedule.objects.filter(is_active=True).select_related("category")[:6]

    return render(request, "academy/home.html", {
        "page": "academy",
        "categories": categories,
        "programs": programs,
        "schedules": schedules,
    })