from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from .forms import CategorySelectionForm

import logging

logger = logging.getLogger(__name__)

def index(request):
    return render(request, "app/index.html")

def products(request):
    products = Product.objects.all() 
    category_selection_form = CategorySelectionForm()
    context = {"products": products,
               "form": category_selection_form}
    if "Hx-Request" in request.headers and request.headers["Hx-Request"]:
        return render(request, "app/partials/products.html", context)

    return render(request, "app/products.html", context)

def help(request):
    return render(request, "app/help.html");
# Create your views here.
