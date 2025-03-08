class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('cart')
        if not cart:
            cart = self.session['cart'] = {}  # Create an empty cart
        self.cart = cart

    def add(self, product, quantity=1, color=None):
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': quantity, 'price': str(product.price), 'color': color}
        else:
            self.cart[product_id]['quantity'] += quantity
            self.cart[product_id]['color'] = color  # Update color if changed
        self.save()

    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def save(self):
        self.session.modified = True

    def get_items(self):
        return self.cart