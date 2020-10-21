from django.views.generic import View
from goods.models import Goods


class GoodsListView(View):  # 重载view完成列表返回
    def get(self, request):
        # 通过django的view实现商品列表页
        json_list = []
        # 获取所有商品
        goods = Goods.objects.all()[:10]

        from django.forms.models import model_to_dict
        # for good in goods:
        #     json_dict = model_to_dict(good)
        #     json_list.append(json_dict)

        from django.core import serializers
        import json

        json_data = serializers.serialize("json", goods)
        # json_data = json.loads(json_data) # pairz1 start

        from django.http import HttpResponse, JsonResponse
        # return HttpResponse(json.dumps(json_data), content_type="application/json") # pairz1 end
        return HttpResponse(json_data, content_type="application/json")
