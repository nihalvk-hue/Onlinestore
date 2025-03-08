from django.contrib import admin
from django.utils.html import format_html
from .models import Order

class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_id', 'name', 'phone', 'email', 'total_price', 'status', 'payment_verified', 'created_at', 'display_payment_screenshot')
    list_filter = ('status', 'created_at', 'payment_verified')
    search_fields = ('order_id', 'name', 'phone', 'email')
    list_editable = ('status', 'payment_verified')  # ✅ Allow inline editing
    readonly_fields = ('display_payment_screenshot',)  

    actions = ['mark_as_shipped', 'mark_as_delivered', 'mark_as_verified']

    def display_payment_screenshot(self, obj):
        """Display payment screenshot as an image preview in the admin panel."""
        if obj.payment_screenshot:
            return format_html(
                '<a href="{}" target="_blank"><img src="{}" width="100" height="100" style="border-radius:5px;" /></a>',
                obj.payment_screenshot.url, obj.payment_screenshot.url
            )
        return "No Screenshot"

    display_payment_screenshot.short_description = "Payment Screenshot"

    def mark_as_shipped(self, request, queryset):
        queryset.update(status='Shipped')
    mark_as_shipped.short_description = "Mark selected orders as Shipped"

    def mark_as_delivered(self, request, queryset):
        queryset.update(status='Delivered')
    mark_as_delivered.short_description = "Mark selected orders as Delivered"

    def mark_as_verified(self, request, queryset):
        queryset.update(payment_verified=True)
    mark_as_verified.short_description = "Mark selected orders as Payment Verified"

admin.site.register(Order, OrderAdmin)