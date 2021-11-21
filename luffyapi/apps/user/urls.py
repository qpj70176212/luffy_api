"""luffyapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, include
from . import views

# 自动生成路由
from rest_framework.routers import SimpleRouter
router = SimpleRouter()
# /user/login 的post请求
router.register('', views.UserView, basename='UserView')
router.register('', views.SmsView, basename='SmsView')
urlpatterns = [
    path('', include(router.urls)),
    path('test/', views.test),

]
# urlpatterns += router.urls