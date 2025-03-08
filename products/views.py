# Create your views here.
from django.shortcuts import render,get_object_or_404
from .models import Product, HeroSection, Category, ProductImage, Color


def home(request):
    hero_section = HeroSection.objects.first()# Get the first hero section
    categories = Category.objects.all()
    latest_products = Product.objects.order_by('-created_at')[:2]  # Get 2 latest products
  
    product = Product.objects.all()  # Get all products
    return render(request, "products/home.html", {"hero_section": hero_section, "categories":categories, "latest_products":latest_products, "product":product})

def product_list(request, category_id=None):
    categories = Category.objects.all()
    query = request.GET.get('q', '')  # Get search query

    if category_id:
        category = get_object_or_404(Category, id=category_id)
        products = Product.objects.filter(category=category)
    else:
        products = Product.objects.all()

    if query:
        products = products.filter(name__icontains=query)  # Filter products by name

    return render(request, "products/product_list.html", {"categories": categories, "products": products, "query": query})

    

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)  # Fetch product by ID
    colors = product.colors.all()
    
    return render(request, 'products/product_detail.html', {'product': product, 'colors':colors})

def contact_view(request):
  return render(request,'products/contact.html')