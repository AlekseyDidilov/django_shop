from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=30, verbose_name="Amazon")
    description = models.TextField(verbose_name="Description")
    rating = models.FloatField(default=0, verbose_name="Rating")
    url = models.URLField(verbose_name="url")

    def __str__(self):
        return self.name


class Laptops(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, verbose_name="Brand")
    description = models.TextField(verbose_name="Description")
    price = models.IntegerField(default=0, verbose_name="Price")

    def __str__(self):
        return self.name
