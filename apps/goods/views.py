from django.shortcuts import render

# Create your views here.
from rest_framework.pagination import PageNumberPagination

from .models import Goods
from .serializer import GoodsSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework import generics


class GoodsPagination(PageNumberPagination):
    """
    good listing page
    """
    page_size = 5
    page_size_query_param = 'page_size'
    page_query_param = 'p'
    max_page_size = 100


class GoodsListView(generics.ListAPIView):
    """
    List all goods
    """

    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    pagination_class = GoodsPagination
