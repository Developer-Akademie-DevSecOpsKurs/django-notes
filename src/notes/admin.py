from django.contrib import admin

from .models import Notes, NotesUser


class NotesUserAdminPanel(admin.ModelAdmin):

    list_display = ("username", "is_staff", "created_at", "updated_at")
    list_filter = ("created_at", "updated_at")
    # readonly_fields = ("date_joined",)


# Register your models here.
admin.site.register(Notes)
admin.site.register(NotesUser, NotesUserAdminPanel)