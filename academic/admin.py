from django.contrib import admin
from academic.models import *

# Register your models here.

@admin.register(AcademicYear)
class AcademicYearAdmin(admin.ModelAdmin):
    list_display = ('year', 'is_active', 'created_at', 'updated_at')
    list_filter = ('is_active',)
    search_fields = ('year',)
    list_editable = ('is_active',)
    ordering = ('-year',)


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')
    search_fields = ('name',)
    ordering = ('name',)