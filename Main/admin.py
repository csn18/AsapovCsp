from django.contrib import admin

from Main.models import Performance, PerformanceName, PerformanceUnit

admin.site.register(PerformanceName)
admin.site.register(PerformanceUnit)


@admin.register(Performance)
class PerformanceAdmin(admin.ModelAdmin):
    list_display = ['cadet', 'name', 'value', 'unit']
    list_filter = ['cadet', 'name']
