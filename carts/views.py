from django.http import JsonResponse
from django.views import View
from carts.mixins import CartMixin
from carts.models import Cart
from goods.models import Products


class CartAddView(CartMixin, View):
    def post(self, request):
        product_id = request.POST.get("product_id")
        
        # Ensure product exists
        try:
            product = Products.objects.get(id=product_id)
        except Products.DoesNotExist:
            return JsonResponse({"message": "Product not found"}, status=404)

        # Get the user's cart or create a new one
        cart = self.get_cart(request, product=product)

        if cart:
            cart.quantity += 1
            cart.save()
        else:
            Cart.objects.create(
                user=request.user if request.user.is_authenticated else None,
                session_key=request.session.session_key if not request.user.is_authenticated else None,
                product=product,
                quantity=1
            )
        
        response_data = {
            "message": "Product added to the cart",
            "cart_items_html": self.render_cart(request)
        }

        return JsonResponse(response_data)


class CartChangeView(CartMixin, View):
    def post(self, request):
        cart_id = request.POST.get("cart_id")
        
        # Ensure cart exists
        cart = self.get_cart(request, cart_id=cart_id)

        # Safely update quantity, ensuring it's a valid integer
        try:
            quantity = int(request.POST.get("quantity"))
        except (ValueError, TypeError):
            return JsonResponse({"message": "Invalid quantity"}, status=400)

        cart.quantity = quantity
        cart.save()

        response_data = {
            "message": "Quantity changed",
            "quantity": cart.quantity,
            "cart_items_html": self.render_cart(request)
        }

        return JsonResponse(response_data)


class CartRemoveView(CartMixin, View):
    def post(self, request):
        cart_id = request.POST.get("cart_id")
        
        # Ensure cart exists
        cart = self.get_cart(request, cart_id=cart_id)
        quantity = cart.quantity
        cart.delete()

        response_data = {
            "message": "Product removed from the cart",
            "quantity_deleted": quantity,
            "cart_items_html": self.render_cart(request)
        }

        return JsonResponse(response_data)