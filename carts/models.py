from django.db import models
from goods.models import Products
from users.models import User


class CartQueryset(models.QuerySet):
    
    def total_price(self):
        """Calculate the total price of all items in the cart."""
        return sum(cart.products_price() for cart in self)
    
    def total_quantity(self):
        """Calculate the total quantity of items in the cart."""
        return sum(cart.quantity for cart in self) if self else 0
    

class Cart(models.Model):

    user = models.ForeignKey(to=User, on_delete=models.CASCADE, blank=True, null=True, verbose_name='User')
    product = models.ForeignKey(to=Products, on_delete=models.CASCADE, verbose_name='Product')
    quantity = models.PositiveSmallIntegerField(default=0, verbose_name='Quantity')
    session_key = models.CharField(max_length=32, null=True, blank=True)
    created_timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Added on')

    class Meta:
        db_table = 'cart'
        verbose_name = "Cart"
        verbose_name_plural = "Carts"
        ordering = ("id",)

    # Use custom queryset manager
    objects = CartQueryset.as_manager()

    def products_price(self):
        """Calculate the total price for a specific cart item."""
        return round(self.product.sell_price() * self.quantity, 2)

    def __str__(self):
        """String representation of the cart."""
        user_str = f'{self.user.username} | ' if self.user else 'Anonymous Cart | '
        return f'{user_str}Product {self.product.name} | Quantity {self.quantity}'