from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Category, Item


def index(request):
    all_category = Category.objects.all()
    context = {
        'all_category' : all_category,
    }
    return render(request, 'shop/index.html', context )
    
def detail(request, category_id):
    all_items = Item.objects.all()
    context = {
        'all_items' : Item.objects.all(),
    }
    return render(request, 'shop/detail.html', context )

def cart(request):
    all_items = Item.objects.all()
    context = {
        'all_items' : Item.objects.all(),
    }
    return render(request, 'shop/cart.html', context )


# Create your views here.
