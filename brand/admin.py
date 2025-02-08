from django.contrib import admin
from .models import Brand, BrandGallery

class BrandGalleryInline(admin.TabularInline):
    model = BrandGallery
    extra = 1  # Allows adding one gallery image by default

class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'slogan')  # Display name and slogan in admin
    search_fields = ('name',)  # Enable search by name
    list_filter = ('slogan',)  # Enable filtering by slogan
    inlines = [BrandGalleryInline]  # Adds the gallery inline form to the Brand admin

admin.site.register(Brand, BrandAdmin)




