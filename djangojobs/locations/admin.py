from django.contrib import admin

from .models import Country, Location

class CountryAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'flag')
    list_display_links = ('name', 'code')
    list_filter = ('name', 'code')
    search_fields = ('name', 'code')
    prepopulated_fields = {'slug': ('name',)}
    ordering = ['-name']

class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'flag')
    list_display_links = ('name', 'country')
    list_filter = ('name', 'country')
    search_fields = ('name', 'country')
    prepopulated_fields = {'slug': ('name',)}
    ordering = ['-name']


admin.site.register(Country, CountryAdmin)
admin.site.register(Location, LocationAdmin)
    
