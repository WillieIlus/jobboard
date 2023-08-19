from django.contrib import admin
# import slugify
from django.utils.text import slugify
from .models import Plan


@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    list_display = ('title', 'price_per_day', 'is_default', 'is_fallback', 'is_available', 'is_active', 'is_featured', 'weight', 'created', 'updated')
    list_filter = ('is_default', 'is_fallback', 'is_available', 'is_active', 'is_featured')
    search_fields = ('title', 'description')
    readonly_fields = ('created', 'updated')
    # fieldsets = ('Plan Details', {'fields': ('title', 'description', 'price_per_day', 'trial_period', 'is_default', 'is_fallback', 'is_available', 'is_active', 'is_featured', 'weight')}),
    ordering = ('weight',)
    # prepopulated_fields = {'slug': ('title',)}


# admin.site.register(Plan, PlanAdmin)
