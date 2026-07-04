from django.contrib import admin

from gallery.models import Album, Photo

# Register your models here.


class PhotoInline(admin.TabularInline):
    model = Photo
    extra = 1


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "featured",
        "is_published",
        "created_at",
    )

    list_editable = (
        "featured",
        "is_published",
    )

    search_fields = (
        "title",
        "description",
    )

    prepopulated_fields = {
        "slug": ("title",)
    }

    inlines = [
        PhotoInline,
    ]


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):

    list_display = (
        "album",
        "title",
        "order",
    )

    ordering = (
        "album",
        "order",
    )