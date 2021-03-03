
from .models import ProductTable
import django_filters


class ProductTableFilter(django_filters.FilterSet):
    ProductName = django_filters.CharFilter(lookup_expr='iexact')
    sname = django_filters.CharFilter(lookup_expr='iexact')
    category_name = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        Model = ProductTable
        fields = ['ProductName', 'sname', 'category_name']
