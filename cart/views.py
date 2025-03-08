from django.shortcuts import redirect, render, get_object_or_404
from products.models import Product, Color  # Import Color model if needed
from .cart import Cart

def cart_view(request):
    cart = Cart(request)
    cart_items = []
    for product_id, item in cart.get_items().items():
        product = get_object_or_404(Product, id=product_id)
        color = None

        # Fetch color object if stored in the cart
        if 'color' in item and item['color']:
            color = get_object_or_404(Color, id=item['color'])

        cart_items.append({
            'product': product,
            'quantity': item['quantity'],
            'price': item['price'],
            'color': color  # Store the color object
        })

    return render(request, 'cart/cart_view.html', {'cart_items': cart_items})

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart = Cart(request)

    # Get selected color from GET request
    color_id = request.GET.get('color', None)

    cart.add(product, color=color_id)
    return redirect('cart_view')

def remove_from_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart = Cart(request)
    cart.remove(product)
    return redirect('cart_view')