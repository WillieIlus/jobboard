from django.contrib import admin

# Register your models here.
from .models import Job, Impression, Click


class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'company', 'location', 'job_type', 'salary',  'featured', 'paid', 'active')
    list_display_links = ('title', 'author')
    list_filter = ('author', 'company', 'location', 'job_type', 'salary',  'featured', 'paid', 'active')
    search_fields = ('title', 'author', 'company', 'location', 'job_type', 'salary',  'featured', 'paid', 'active')
    prepopulated_fields = {'slug': ('title',)}
    ordering = ['-created_at']

class ImpressionAdmin(admin.ModelAdmin):
    list_display = ('job', 'source_ip', 'session_id', 'timestamp')
    list_display_links = ('job', 'source_ip')
    list_filter = ('job', 'source_ip', 'session_id', 'timestamp')
    search_fields = ('job', 'source_ip', 'session_id', 'timestamp')
    ordering = ['-timestamp']

class ClickAdmin(admin.ModelAdmin):
    list_display = ('job', 'source_ip', 'session_id', 'timestamp')
    list_display_links = ('job', 'source_ip')
    list_filter = ('job', 'source_ip', 'session_id', 'timestamp')
    search_fields = ('job', 'source_ip', 'session_id', 'timestamp')
    ordering = ['-timestamp']

admin.site.register(Job, JobAdmin)
admin.site.register(Impression, ImpressionAdmin)
admin.site.register(Click, ClickAdmin)
