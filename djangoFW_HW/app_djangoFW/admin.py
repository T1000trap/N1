from django.contrib import admin
from .models import Advertisment

class AdvertismentAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "description", "price", "auction", "created_date"]
    list_filter = ["auction", "created_at"]
    actions = ["make_aktions_as_false", "make_aktions_as_true"]
    fieldsets = (
        ("Общее", {
            "fields": ("title", "description"),
        }),
        ("Финансы", {
            "fields": ("price", "auction"),
            "classes": ["collapse"]
        })
    )

    @admin.action(description="Убрать торг")
    def make_aktions_as_false(self, request, queryset):
        queryset.update(auction=False)

    @admin.action(description="Добавить торг")
    def make_aktions_as_true(self, request, queryset):
        queryset.update(auction=True)


admin.site.register(Advertisment, AdvertismentAdmin)
