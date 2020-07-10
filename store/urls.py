from django.urls import path
from store.views import index, cart, checkout, product, updateItem, processOrder


urlpatterns = [
    path('', index, name="index"),
    path('product/', product, name="product"),
    path('cart/', cart, name="cart"),
    path('checkout/', checkout, name="checkout"),

    path('update_item/', updateItem, name="update_item"),
    path('process_order/', processOrder, name="process_order"),
]
