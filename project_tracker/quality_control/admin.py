from django.contrib import admin

from .models import BugReport, FeatureRequest


def change_status_to_Completed(modeladmin, request, queryset):
    queryset.update(status='Completed')


change_status_to_Completed.short_description = 'Поменять статус на "Завершена"'


def change_status_to_New(modeladmin, request, queryset):
    queryset.update(status='New')


change_status_to_New.short_description = 'Поменять статус на "Новая"'


def change_status_to_In_progress(modeladmin, request, queryset):
    queryset.update(status='In_progress')


change_status_to_In_progress.short_description = 'Поменять статус на "В процессе"'


@admin.register(BugReport)
class BugReportAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at',)
    list_filter = ('project', 'task', 'status', 'priority',)
    search_fields = ('title', 'description',)
    actions = [change_status_to_Completed, change_status_to_New, change_status_to_In_progress]
    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'created_at',)
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('project', 'task', 'status', 'priority',),
        }),
    )
    readonly_fields = ('created_at', 'updated_at',)



@admin.register(FeatureRequest)
class FeatureRequestAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at',)
    list_filter = ('project', 'task', 'status', 'priority',)
    search_fields = ('title', 'description',)
    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'created_at',)
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('project', 'task', 'status', 'priority',),
        }),
    )
    readonly_fields = ('created_at', 'updated_at',)