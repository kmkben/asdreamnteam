from django.shortcuts import render


def donation(request):

    return render(
        request,
        "donation/donation.html",
        {
            "page": "donation",
        },
    )