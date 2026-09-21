from django.urls import path
from . import views


urlpatterns = [
    path('product/', views.product, name='prduct-details' ),
    path('shop/', views.shop, name='shop')
]