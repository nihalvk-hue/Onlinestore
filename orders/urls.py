from django.urls import path
from .views import checkout, order_success, track_order, buy_product

urlpatterns = [
    path('checkout/', checkout, name='checkout'),
    path('track/', track_order, name='track_order'),
    path('buy/<int:product_id>/', buy_product, name='buy_product'),
    path("success/<int:product_id>/", order_success, name="order_success"),
]




