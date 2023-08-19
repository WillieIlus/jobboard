from django.contrib import admin


from .models import Company

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'location', 'phone', 'website', 'email')
    list_display_links = ('name', 'user')
    list_filter = ('user', 'location')
    search_fields = ('name', 'user', 'location', 'phone', 'website', 'email')
    prepopulated_fields = {'slug': ('name',)}
    ordering = ['-name']

admin.site.register(Company, CompanyAdmin)


