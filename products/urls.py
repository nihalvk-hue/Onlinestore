from django.urls import path
from .views import product_list, product_detail,home,contact_view

urlpatterns = [
    path('product_list/', product_list, name='product_list'),
    path('<int:product_id>/', product_detail, name='product_detail'),
    path('', home, name='home'),
    path('category/<int:category_id>/', product_list, name='category_products'),
    path('contact/',contact_view, name='contact')

]
