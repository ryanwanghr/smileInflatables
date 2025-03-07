from django.urls import path
from . import views

app_name = "app"

urlpatterns = [
    path('', views.index, name="index"),
    path('products', views.products, name="products"),
    path('help', views.help, name="help"),
]
