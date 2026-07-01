from django.shortcuts import render

from academy.models import TrainingCategory


def categories(request):

    context = {
        "page": "academy",
        "categories": TrainingCategory.objects.filter(
            is_active=True
        ).order_by("order"),
    }

    return render(
        request,
        "academy/categories.html",
        context,
    )