from django.shortcuts import render, get_list_or_404
from .models import Category, Product

def product_list(request, category_slug =None):
    category =None 
    categories =Category.objects.all()
    