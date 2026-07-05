from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import redirect, render

from contact.forms import ContactForm


def contact(request):
    form = ContactForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        full_name = form.cleaned_data["full_name"]
        sender_email = form.cleaned_data["email"]
        subject = form.cleaned_data["subject"]
        message = form.cleaned_data["message"]

        email_subject = f"[{settings.SITE_NAME}] {subject}"

        email_message = f"""
Nouveau message depuis le site {settings.SITE_NAME}

Nom : {full_name}
Email : {email}

Message :
{message}
"""

        # send_mail(
        #     subject=subject,
        #     message=message,
        #     from_email=settings.DEFAULT_FROM_EMAIL,
        #     recipient_list=[settings.ADMIN_EMAIL],
        #     fail_silently=False,
        # )
        
        email = EmailMessage(
            subject=email_subject,
            body=email_message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[settings.ADMIN_EMAIL],
            reply_to=[sender_email],
        )

        email.send(fail_silently=False)

        messages.success(
            request,
            "Votre message a bien été envoyé. Nous vous répondrons dès que possible.",
        )

        return redirect("contact:contact")

    return render(request, "contact/contact.html", {
        "page": "contact",
        "form": form,
    })