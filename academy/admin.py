from django.contrib import admin

from academy.models import TrainingCategory, TrainingProgram, TrainingSchedule

# Register your models here.



@admin.register(TrainingCategory)
class TrainingCategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "short_name", "min_age", "max_age", "is_active", "order")
    list_filter = ("is_active",)
    search_fields = ("name", "short_name", "description")
    list_editable = ("is_active", "order")
    ordering = ("order", "min_age")


@admin.register(TrainingProgram)
class TrainingProgramAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "is_active", "order")
    list_filter = ("category", "is_active")
    search_fields = ("title", "description", "objectives")
    list_editable = ("is_active", "order")
    ordering = ("order", "title")


@admin.register(TrainingSchedule)
class TrainingScheduleAdmin(admin.ModelAdmin):
    list_display = ("category", "day", "start_time", "end_time", "location", "is_active")
    list_filter = ("category", "day", "is_active")
    search_fields = ("category__name", "location", "note")
    list_editable = ("is_active",)
    ordering = ("category", "day", "start_time")
