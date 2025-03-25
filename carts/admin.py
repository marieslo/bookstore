from django.contrib import admin
from .models import Cart


# Inline cart admin for displaying cart items
class CartTabAdmin(admin.TabularInline):
    model = Cart
    fields = ("product", "quantity", "created_timestamp")
    search_fields = ("product", "quantity", "created_timestamp")
    readonly_fields = ("created_timestamp",)
    extra = 1


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    # Display configuration for the Cart model in the admin panel
    list_display = ("user_display", "product_display", "quantity", "created_timestamp")
    list_filter = ("created_timestamp", "user", "product__name")

    # Display user as a string, with fallback to "Anonymous User"
    def user_display(self, obj):
        return str(obj.user) if obj.user else "Anonymous User"

    # Display product name in the admin panel
    def product_display(self, obj):
        return str(obj.product.name)

    # Customize column names in the admin interface
    user_display.short_description = "User"
    product_display.short_description = "Product"