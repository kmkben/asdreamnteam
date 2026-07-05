from django import forms


class MembershipRequestForm(forms.Form):
    # class PlayerAgeCategory(forms.TextChoices):
    #     U9 = "U9", "U9"
    #     U11 = "U11", "U11"
    #     U13 = "U13", "U13"
    #     U15 = "U15", "U15"
    #     U17 = "U17", "U17"
    #     U20 = "U20", "U20"
    #     SENIOR = "SENIOR", "Senior"
    #     OTHER = "OTHER", "Autre"

    PLAYER_AGE_CATEGORIES = [
        ("U9", "U9"),
        ("U11", "U11"),
        ("U13", "U13"),
        ("U15", "U15"),
        ("U17", "U17"),
        ("U20", "U20"),
        ("SENIOR", "Senior"),
        ("OTHER", "Autre"),
    ]

    full_name = forms.CharField(
        label="Nom complet du joueur",
        max_length=150,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Nom complet",
        }),
    )

    age = forms.IntegerField(
        label="Âge",
        min_value=5,
        max_value=60,
        widget=forms.NumberInput(attrs={
            "class": "form-control",
            "placeholder": "Âge",
        }),
    )

    category = forms.ChoiceField(
        label="Catégorie souhaitée",
        choices=PLAYER_AGE_CATEGORIES,
        widget=forms.Select(attrs={
            "class": "form-select",
        }),
    )

    phone = forms.CharField(
        label="Téléphone",
        max_length=50,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "+229 ...",
        }),
    )

    email = forms.EmailField(
        label="Email",
        required=False,
        widget=forms.EmailInput(attrs={
            "class": "form-control",
            "placeholder": "email@example.com",
        }),
    )

    guardian_name = forms.CharField(
        label="Nom du parent/tuteur",
        required=False,
        max_length=150,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Obligatoire si joueur mineur",
        }),
    )

    message = forms.CharField(
        label="Message",
        required=False,
        widget=forms.Textarea(attrs={
            "class": "form-control",
            "rows": 5,
            "placeholder": "Informations complémentaires...",
        }),
    )