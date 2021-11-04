from django.shortcuts import render, HttpResponse
from rest_framework.views import APIView
# Create your views here.
from luffyapi.utils.logger import get_logger
from luffyapi.utils.response import APIResponse

logger = get_logger('django')


def test_logger(request):
    logger.info('请求来了')
    return HttpResponse('ok')


class TestView(APIView):
    def get(self, request):
        l = [1, 2, 3]
        print(l[9])
        return APIResponse()


## 轮播图接口
from rest_framework.viewsets import ViewSetMixin
from rest_framework.generics import ListAPIView
from .serializer import BannerSerializer
from .models import Banner
from django.conf import settings

class BannerView(ViewSetMixin, ListAPIView):
    queryset = Banner.objects.all().filter(is_show=True, is_delete=False).order_by('-orders')[0:settings.BANNER_SIZE]
    serializer_class = BannerSerializer
