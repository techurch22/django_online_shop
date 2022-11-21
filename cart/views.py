from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST
from electronic_shop.shop.models import Product
from cart import Cart
from forms import CartAddProductForm

@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        safe_data = form.cleaned_data
        cart.add(product=product, quantity=safe_data['quantity'], update_quantity=safe_data['update'])

    return redirect
