from django.db import models


def cat_upload_directory(instance, filename):
    return f"category/{filename}"

def product_upload_directory(instance, filename):
    return f"product/{filename}"

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=20)
    image = models.ImageField(default='default.jpg', upload_to=cat_upload_directory)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(default='default.jpg', upload_to=product_upload_directory)
    description = models.TextField()
    price = models.FloatField()
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.name