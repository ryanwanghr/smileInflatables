from django.db import models


# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=200)
    product_image_url = models.FileField(upload_to="media/")

    def __str__(self):
        return self.product_name
