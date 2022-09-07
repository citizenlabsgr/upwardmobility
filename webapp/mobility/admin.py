from django.contrib import admin
from mobility.models import *
# Register your models here.

admin.site.site_header = 'Upward Mobility'


class SubSectionInline(admin.StackedInline):
    model = SubSection
    extra = 1


@admin.register(Post)
class QuillPostAdmin(admin.ModelAdmin):
    list_display = ("title", "text",)
    prepopulated_fields = {"slug": ("title",)}
    inlines = [
        SubSectionInline
        ]
