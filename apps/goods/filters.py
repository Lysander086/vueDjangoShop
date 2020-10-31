import django_filters

from .models import Goods


class GoodsFilter(django_filters.rest_framework.FilterSet):
    pricemin = django_filters.NumberFilter(name="shop_price", lookup_expr='gte', help_text='最小价格')
    pricemax = django_filters.NumberFilter(name="shop_price", lookup_expr='lte')

    # name = django_filters.CharFilter(name='name', lookup_expr='icontains')

    class Meta:
        model = Goods
        fields = ['pricemin', 'pricemax']
