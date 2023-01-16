from django.urls import path
from .views import CartView, AddCartView, RemoveCartView, RemoveCartItemView

urlpatterns = [
    path('', CartView.as_view(), name="cart_view"),
    path('add_cart/<int:product_id>/', AddCartView.as_view(), name="add_cart"),
    path('remove_cart/<int:product_id>/', RemoveCartView.as_view(), name="remove_cart"),
    path('remove_cart_item/<int:product_id>/', RemoveCartItemView.as_view(), name="remove_cart_item"),
]