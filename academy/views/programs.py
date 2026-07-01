from django.shortcuts import render

from academy.models import TrainingProgram


def programs(request):

    context = {
        "page": "academy",
        "programs": TrainingProgram.objects.filter(
            is_active=True
        ).select_related("category").order_by("order"),
    }

    return render(
        request,
        "academy/programs.html",
        context,
    )