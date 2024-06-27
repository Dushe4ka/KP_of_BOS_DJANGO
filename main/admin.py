from django.contrib import admin

from main.models import Message


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ("id", "date_m", "info_m", "application_m", "action_m")
    list_filter = ("info_m",)
