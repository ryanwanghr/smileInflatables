# Generated by Django 5.0.6 on 2024-06-13 03:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_product_product_image_url'),
    ]

    operations = [
        migrations.RenameField("Product", "product_image_url", "product_image"),
    ]
