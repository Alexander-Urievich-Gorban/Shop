import django_filters
from .models import Product


class ProductFilter(django_filters.FilterSet):
    CHOICES = (
        ('increasing', 'По увеличению цены'),
        ('decreasing', 'По уменьшению цены')
    )
    price_ordering = django_filters.ChoiceFilter(label='', choices=CHOICES,
                                                 method='filter_by_order')

    def filter_by_order(self, queryset, name, value):
        expression = '-price' if value == 'increasing' else 'price'
        return queryset.order_by(expression)
