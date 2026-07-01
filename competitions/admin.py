from django.contrib import admin

from competitions.models import Competition, Match

# Register your models here.



@admin.register(Competition)
class CompetitionAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "season",
        "is_active",
        "order",
    )
    list_filter = (
        "season",
        "is_active",
    )
    search_fields = (
        "name",
        "description",
        "season",
    )
    list_editable = (
        "is_active",
        "order",
    )
    ordering = (
        "order",
        "name",
    )


@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    list_display = (
        "competition",
        "opponent",
        "match_date",
        "location",
        "home_match",
        "status",
        "score_display",
    )
    list_filter = (
        "competition",
        "status",
        "home_match",
        "match_date",
    )
    search_fields = (
        "opponent",
        "location",
        "note",
    )
    date_hierarchy = "match_date"
    ordering = (
        "-match_date",
    )

    @admin.display(description="Score")
    def score_display(self, obj):
        if obj.our_score is None or obj.opponent_score is None:
            return "-"
        return f"{obj.our_score} - {obj.opponent_score}"
