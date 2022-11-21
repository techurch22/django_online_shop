from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Category, Product


class ProductViewList(View):
    def get(self, request, category_slug=None, *args, **kwargs):
        category = None
        categories = Category.objects.all()
        products = Product.objects.filter(available=True)
        if category_slug:
            category = get_object_or_404(Category, slug=category_slug)
            products = Product.objects.filter(category=category)

        return render(request, 'shop.html', context={
            'category': category,
            'categories': categories,
            'products': products,
        })


class ProductDetailView(View):
    def get(self, request, product_id, product_slug):
        product = get_object_or_404(Product, id=product_id, slug=product_slug, available=True)
        categories = Category.objects.all()

        return render(request, 'product.html', context={
            'product': product,
            'categories': categories,
        })

