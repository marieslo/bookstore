# users/admin.py
from django.contrib import admin
from carts.admin import CartTabAdmin
from users.models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["username", "first_name", "last_name", "email"]
    search_fields = ["username", "first_name", "last_name", "email"]

    inlines = [CartTabAdmin]

    # Lazy import of OrderTabulareAdmin to avoid circular import
    def get_inlines(self, request, obj=None):
        from orders.admin import OrderTabulareAdmin
        return self.inlines + [OrderTabulareAdmin]