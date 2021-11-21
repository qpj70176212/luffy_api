from django.shortcuts import render, HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.
from luffyapi.utils.logger import get_logger
from luffyapi.utils.response import APIResponse
from django.core.cache import cache

# logger = get_logger('django')
logger = get_logger()


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

    # 重写list方法 接口缓存
    def list(self, request, *args, **kwargs):
        banner_list = cache.get('banner_cache_list')
        # 如果没有值，去数据库查
        if not banner_list:
            response = super().list(request, *args, **kwargs)
            # 在缓存中放一份
            cache.set('banner_cache_list', response.data)
        else:
            # 走了缓存，速度很快
            print('走了缓存')
            response = Response(data=banner_list)

        return response
