from django.urls import path
from .views import productListAPIView


urlpatterns = [
   # path('product/', views.product, name='product' ),
    #path('shop/', views.shop, name='shop')
    path("shop", list_products.as_view(), name="products"),
    path("shop/<int:pk>", product_detail.as_view(), name="product_detail"),
]