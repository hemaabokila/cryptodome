from django.contrib import admin
from .models import Blog,AppVisit


admin.site.register(Blog)

@admin.register(AppVisit)
class AppVisitAdmin(admin.ModelAdmin):
    list_display = ('app_name', 'date', 'visit_count')
    list_filter = ('app_name', 'date')

