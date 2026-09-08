from django.contrib import admin

from news.models import NewsArticle

# Register your models here.


@admin.register(NewsArticle)
class ArticleAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "featured",
        "is_published",
        "published_at",
    )

    list_filter = (
        "featured",
        "is_published",
        "published_at",
    )

    search_fields = (
        "title",
        "summary",
        "content",
    )

    prepopulated_fields = {
        "slug": ("title",)
    }

    list_editable = (
        "featured",
        "is_published",
    )

    ordering = (
        "-published_at",
    )