from django import forms


class ContactForm(forms.Form):
    full_name = forms.CharField(
        label="Nom complet",
        max_length=150,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Votre nom complet",
        }),
    )

    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(attrs={
            "class": "form-control",
            "placeholder": "votre@email.com",
        }),
    )

    subject = forms.CharField(
        label="Sujet",
        max_length=150,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Sujet du message",
        }),
    )

    message = forms.CharField(
        label="Message",
        widget=forms.Textarea(attrs={
            "class": "form-control",
            "placeholder": "Votre message...",
            "rows": 6,
        }),
    )