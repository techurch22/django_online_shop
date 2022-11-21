from django.urls import path
from .views import ProductViewList, ProductDetailView


urlpatterns = [
    path('', ProductViewList.as_view(), name='all_product_view'),
    path('<str:category_slug>/', ProductViewList.as_view(), name='cat_product_view'),
    path('<int:product_id>/<str:product_slug>/', ProductDetailView.as_view(), name='product_view'),
]