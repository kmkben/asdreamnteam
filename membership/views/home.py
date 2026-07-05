from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail, EmailMessage
from django.shortcuts import redirect, render

from membership.forms import MembershipRequestForm


def home(request):
    form = MembershipRequestForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        data = form.cleaned_data
        # sender_email = form.cleaned_data["email"]

        subject = f"[{settings.SITE_NAME}] Nouvelle demande d'inscription"

        message = f"""
Nouvelle demande d'inscription depuis le site {settings.SITE_NAME}

Joueur : {data["full_name"]}
Âge : {data["age"]}
Catégorie souhaitée : {data["category"]}

Téléphone : {data["phone"]}
Email : {data["email"] or "Non renseigné"}
Parent/Tuteur : {data["guardian_name"] or "Non renseigné"}

Message :
{data["message"] or "Aucun message"}
"""

        # send_mail(
        #     subject=subject,
        #     message=message,
        #     from_email=settings.DEFAULT_FROM_EMAIL,
        #     recipient_list=[settings.ADMIN_EMAIL],
        #     fail_silently=False,
        # )
        
        reply_to = [data["email"]] if data["email"] else []
        
        email = EmailMessage(
            subject=subject,
            body=message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[settings.ADMIN_EMAIL],
            reply_to=reply_to,
        )

        email.send(fail_silently=False)

        messages.success(
            request,
            "Votre demande d'inscription a bien été envoyée. Le club vous contactera prochainement.",
        )

        return redirect("membership:home")

    return render(request, "membership/home.html", {
        "page": "membership",
        "form": form,
    })