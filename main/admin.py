from django.contrib import admin

from .models import FAQ
from .models import Privacy
from .models import Term
from .models import Service, SubService, SubServiceImage

# Register your models here.
import csv
from django.http import HttpResponse
from .models import NewsletterSubscription

@admin.register(NewsletterSubscription)
class NewsletterSubscriptionAdmin(admin.ModelAdmin):
    list_display = ('email', 'subscribed_at')
    search_fields = ('email',)
    list_filter = ('subscribed_at',)
    ordering = ('-subscribed_at',)

    actions = ['export_to_csv']

    def export_to_csv(self, request, queryset):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="newsletter_subscriptions.csv"'
        writer = csv.writer(response)

        # Write the header row
        writer.writerow(['Email', 'Subscribed At'])

        # Write the data rows
        for subscription in queryset:
            writer.writerow([subscription.email, subscription.subscribed_at])

        return response

    export_to_csv.short_description = "Export to CSV"


from import_export.admin import ExportMixin

class ContactMessageAdmin(ExportMixin, admin.ModelAdmin):
    list_display = ("first_name", "email", "phone", "submitted_at")
    search_fields = ("first_name", "email", "phone")
    list_filter = ("submitted_at",)
    ordering = ("-submitted_at",)
    readonly_fields = ("first_name", "email", "phone", "message", "submitted_at")

    fieldsets = (
        (None, {
            "fields": ("first_name", "email", "phone", "message")
        }),
        ("Metadata", {
            "fields": ("submitted_at",),
        }),
    )



@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'created_at', 'updated_at')
    search_fields = ('question',)
    list_filter = ('created_at',)

@admin.register(Privacy)
class PrivacyAdmin(admin.ModelAdmin):
    list_display = ('privacy', 'created_at', 'updated_at')
    search_fields = ('privacy',)
    list_filter = ('created_at',)

@admin.register(Term)
class TermAdmin(admin.ModelAdmin):
    list_display = ('term', 'created_at', 'updated_at')
    search_fields = ('term',)
    list_filter = ('created_at',)

# admin.py

class SubServiceInline(admin.TabularInline):
    model = SubService
    extra = 1

class SubServiceImageInline(admin.TabularInline):
    model = SubServiceImage
    extra = 1

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    inlines = [SubServiceInline]

@admin.register(SubService)
class SubServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'service')
    inlines = [SubServiceImageInline]

@admin.register(SubServiceImage)
class SubServiceImageAdmin(admin.ModelAdmin):
    list_display = ('sub_service', 'image')


from django.contrib import admin
from .models import Brochure

@admin.register(Brochure)
class BrochureAdmin(admin.ModelAdmin):
    list_display = ('title', 'uploaded_at')
