from django.core.validators import FileExtensionValidator
from django.db import models
from django.db.models import Avg, Count
from django.urls import reverse
from django.utils.functional import cached_property
from django.conf import settings
from django.contrib.auth.models import User


class Category(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    image = models.ImageField(upload_to='category/')

    def __str__(self):
        return self.title

    def get_products(self):
        return self.product_category.all()

    def get_absolute_url(self):
        return reverse('category_list', kwargs={'slug': self.slug})


class Product(models.Model):
    title = models.CharField("Названию", max_length=100)
    description = models.TextField()
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to='product/')
    category = models.ForeignKey(Category, related_name='product_category', on_delete=models.SET_NULL, null=True,
                                 blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product_detail', kwargs={'pk': self.id})

    class Meta:
        ordering = ('price',)


class Basket(models.Model):
    product = models.ForeignKey(Product, related_name='product_category', on_delete=models.SET_NULL, null=True,
                                blank=True)
    count_products = models.SmallIntegerField(default=0)
    cost = models.IntegerField(default=0)
