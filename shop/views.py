from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Category, Product
from cart.forms import CartAddProductForm
from cart.views import Cart


class ProductViewList(View):
    def get(self, request, category_slug=None, *args, **kwargs):
        category = None
        categories = Category.objects.all()
        products = Product.objects.filter(available=True)
        if category_slug:
            category = get_object_or_404(Category, slug=category_slug)
            products = Product.objects.filter(category=category)

        cart = Cart(request)

        return render(request, 'shop/shop.html', context={
            'category': category,
            'categories': categories,
            'products': products,
            'cart': cart,
        })


class ProductDetailView(View):
    def get(self, request, product_id, product_slug):
        product = get_object_or_404(Product, id=product_id, slug=product_slug, available=True)
        categories = Category.objects.all()

        cart_form = CartAddProductForm()
        cart = Cart(request)

        return render(request, 'shop/product.html', context={
            'product': product,
            'categories': categories,
            'cart_form': cart_form,
            'cart': cart
        })

