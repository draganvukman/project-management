from django.contrib import admin
from .models import Message

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('sender', 'receiver', 'subject', 'timestamp', 'is_archived')
    list_filter = ('is_archived', 'timestamp')