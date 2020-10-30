# Create your views here.
from rest_framework import viewsets, mixins
from rest_framework.pagination import PageNumberPagination

from .models import Goods
from .serializer import GoodsSerializer


class GoodsPagination(PageNumberPagination):
    """
    good listing page
    """
    page_size = 5
    page_size_query_param = 'page_size'
    page_query_param = 'p'
    max_page_size = 100


# class GoodsListViewSet(viewsets.ModelViewSet):
class GoodsListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    List all goods
    """
    serializer_class = GoodsSerializer
    pagination_class = GoodsPagination

    def get_queryset(self):
        query_set = Goods.objects.all()
        price_min = self.request.query_params.get('price_min', 0)
        if price_min:
            query_set = query_set.filter(shop_price__gt=int(price_min))
        return query_set
