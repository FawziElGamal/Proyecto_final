from .cart import Cart

def quantity_products_cart(request):
    cart = Cart(request)
    quantity = cart.print_items()

    return {'quantity': quantity}