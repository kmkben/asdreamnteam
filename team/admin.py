from django.contrib import admin

from team.models import ClubMember
from team.models import Sponsor
from team.models import Partner
# Register your models here.
 

@admin.register(ClubMember)
class ClubMemberAdmin(admin.ModelAdmin):
    list_display = (
        "full_name",
        "role",
        "position",
        "category",
        "is_active",
        "order",
    )
    list_filter = (
        "role",
        "category",
        "is_active",
    )
    search_fields = (
        "first_name",
        "last_name",
        "position",
        "category",
    )
    list_editable = (
        "is_active",
        "order",
    )
    ordering = (
        "order",
        "last_name",
        "first_name",
    )


@admin.register(Sponsor)
class SponsorAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "website",
        "is_active",
        "order",
    )
    list_filter = (
        "is_active",
    )
    search_fields = (
        "name",
        "description",
    )
    list_editable = (
        "is_active",
        "order",
    )
    ordering = (
        "order",
        "name",
    )


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "website",
        "is_active",
        "order",
    )
    list_filter = (
        "is_active",
    )
    search_fields = (
        "name",
        "description",
    )
    list_editable = (
        "is_active",
        "order",
    )
    ordering = (
        "order",
        "name",
    )