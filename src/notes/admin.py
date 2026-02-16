from django.contrib import admin

from .models import Note, NotesUser


class NotesUserAdminPanel(admin.ModelAdmin):

    list_display = ("username", "is_staff", "created_at", "updated_at")
    list_filter = ("created_at", "updated_at")
    # readonly_fields = ("date_joined",)

class NotesAdminPanel(admin.ModelAdmin):
    list_display = ("id", "title", "created_by")
    list_filter = ("created_by", "title")
    sortable_by = ("created_by", "title")

# Register your models here.
admin.site.register(Note, NotesAdminPanel)
admin.site.register(NotesUser, NotesUserAdminPanel)