import os
from django.db import models
from django.utils import timezone



# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.category_name

def format_product(instance, filename):
    base_filename, ext = os.path.splitext(filename)
    timestamp = timezone.now().strftime("%Y%m%d_%H%M%S")

    new_filename = f"{timestamp}_{base_filename}{ext}"
    return new_filename

class Product(models.Model):
    product_name = models.CharField(max_length=200)
    product_image = models.ImageField(max_length=300,upload_to=format_product)
    product_category = models.ManyToManyField(Category)
    product_description = models.TextField(default="")
    
    def delete(self):
        self.product_image.delete()
        super().delete()

    def __str__(self):
        return self.product_name

