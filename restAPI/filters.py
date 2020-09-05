import django_filters
from restAPI.models import *


class CategoryFilter(django_filters.BaseInFilter, django_filters.CharFilter):
    pass


class PriceFilter(django_filters.FilterSet):
    category_filter = CategoryFilter(
        field_name='category__title', lookup_expr='in')
    price = django_filters.RangeFilter()

    class Meta:
        model = Product
        fields = ['price', 'category_filter']
