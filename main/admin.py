from django.contrib import admin
from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.models import FlatPage
from django.db import models
from django.utils.translation import gettext_lazy as _

from ckeditor.widgets import CKEditorWidget


from .models import Category, Book, BookFile, CustomFlatePage, Application
from .forms import CustomFlatePageForm


class FlatPageCustom(FlatPageAdmin):
    form = CustomFlatePageForm
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "url",
                    "title",
                    "content",
                    "sites",
                    "cover",
                )
            },
        ),
        (
            _("Advanced options"),
            {
                "classes": ("collapse",),
                "fields": ("registration_required", "template_name"),
            },
        ),
    )
    formfield_overrides = {models.TextField: {"widget": CKEditorWidget}}


admin.site.unregister(FlatPage)
admin.site.register(CustomFlatePage, FlatPageCustom)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Административная панель для Категорий (с автослагом)"""

    list_display = ["name", "slug"]
    prepopulated_fields = {"slug": ("name",)}


class FileInline(admin.TabularInline):

    model = BookFile


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "is_published",
        "slug",
    ]

    ordering = ["-created"]
    actions = [
        "make_published",
    ]
    prepopulated_fields = {"slug": ("title",)}

    inlines = (FileInline,)

    def make_published(modeladmin, request, queryset):
        queryset.update(is_published=True)

    make_published.short_description = "Публиковать выбранные объявления"


@admin.register(Application)
class CollectingApplicationsAdmin(admin.ModelAdmin):
    """Административная панель для CollectingApplications"""

    list_display = ["name", "email", "message", "agreement"]
