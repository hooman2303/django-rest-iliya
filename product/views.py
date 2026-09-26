from django.shortcuts import render
from .models import Product
# Create your views here.
def product(req):
    get_prdct = Product.objects.all()
    return render(req, 'shop.html')

def shop(req):
    return render(req, 'product.html')