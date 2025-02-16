from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Project

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_date', 'end_date', 'status')
    filter_horizontal = ('stakeholders',)