from django.shortcuts import render, redirect, get_object_or_404
from .forms import OrderForm
from cart.cart import Cart
from .models import Order,UPI
from products.models import Product, Color, QRCode

def buy_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    color_id = request.GET.get('color')
    selected_color = None
    qr_code = QRCode.objects.first()  
    upi = UPI.objects.first()  

    if color_id and color_id.isdigit():  
        selected_color = get_object_or_404(Color, id=int(color_id))
    
    return render(request, 'orders/checkout.html', {
        'product': product, 
        'selected_color': selected_color, 
        'qr_code': qr_code,
        'upi': upi
    })

    
def checkout(request, product_id, color_id):
    cart = Cart(request)
    qr_code = QRCode.objects.first()
    upi = UPI.objects.first()
    selected_color = get_object_or_404(Color, id=color_id) if color_id else None  

    if request.method == 'POST':
        form = OrderForm(request.POST, request.FILES)  
        if form.is_valid():
            order = form.save(commit=False)
            cart_items = cart.get_items()

            # ✅ Ensure total_price calculation is safe
            order.total_price = sum(float(item.get('price', 0)) * item.get('quantity', 1) for item in cart_items.values())

            if request.FILES.get("payment_screenshot"):  
                order.payment_screenshot = request.FILES["payment_screenshot"]

            color_id = request.POST.get("color")
            if color_id:
                order.selected_color = get_object_or_404(Color, id=color_id)

            order.save()
            cart.clear()  # ✅ Clear cart safely
            return redirect('order_success', product_id=product_id)
    else:
        form = OrderForm()
    
    return render(request, 'orders/checkout.html', {
        'form': form, 
        'qr_code': qr_code, 
        'upi': upi,
        'selected_color': selected_color
    })


def order_success(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        alt_phone = request.POST.get("alt_phone")  # ✅ Get alternative phone
        email = request.POST.get("email")
        address = request.POST.get("address")
        pincode = request.POST.get("pincode")
        upi_transaction_id = request.POST.get("upi_transaction_id")
        color_id = request.POST.get("color")
        payment_screenshot = request.FILES.get("payment_screenshot")  

        selected_color = get_object_or_404(Color, id=color_id) if color_id else None
        total_price = product.price  

        # ✅ Save order with payment_verified=False initially
        order = Order.objects.create(
            name=name,
            phone=phone,
            alt_phone=alt_phone,  # ✅ Save alternative phone
            email=email,
            address=address,
            pincode=pincode,
            upi_transaction_id=upi_transaction_id,
            product=product,
            selected_color=selected_color,  
            payment_screenshot=payment_screenshot,
            total_price=total_price,
            payment_verified=False  
        )

        # ✅ Show pending payment page if not verified
        if not order.payment_verified:
            return render(request, 'orders/payment_pending.html', {'order': order})

        return render(request, 'orders/order_success.html', {'order': order})

    return redirect("product_list")
    
    
def track_order(request):
    order = None
    error = None

    if request.method == "POST":
        phone = request.POST.get("phone")
        order_id = request.POST.get("order_id")

        try:
            if order_id:
                order = get_object_or_404(Order, order_id=order_id)
            elif phone:
                order = Order.objects.filter(phone=phone).order_by('-created_at').first()  # ✅ Get latest order
            else:
                error = "Please enter either your Order ID or Phone Number."
        except Order.DoesNotExist:
            error = "No order found with the given details."

    return render(request, "orders/track_order.html", {"order": order, "error": error})