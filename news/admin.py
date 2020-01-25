from django.contrib import admin

from .models import News


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'posted_date')
    list_filter = ('status',)
    actions = ('publish', 'unpublish')

    def publish(self, request, queryset):
        queryset.update(status='PUBLISHED')

    publish.short_description = "Publish Selected"

    def unpublish(self, request, queryset):
        queryset.update(status='UNPUBLISHED')

    unpublish.short_description = "Unpublish Selected"
