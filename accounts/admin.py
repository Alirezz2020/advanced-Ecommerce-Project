# accounts/admin.py
from django.contrib import admin
from .models import NewsletterSubscription

@admin.register(NewsletterSubscription)
class NewsletterSubscriptionAdmin(admin.ModelAdmin):
    list_display = ('email', 'subscribed_at')  # Display these fields in the admin list view
    search_fields = ('email',)  # Allow searching by email
    list_filter = ('subscribed_at',)  # Optionally filter by the subscription date
