from django import template
from shop.models import Product
register = template.Library()
@register.simple_tag()
def get_products():
    return Product.objects.all()