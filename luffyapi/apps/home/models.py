from django.db import models

# Create your models here.
# from luffyapi.utils.models import BaseModel
from luffyapi.utils.models import BaseModel

class Banner(BaseModel):
    title = models.CharField(max_length=16, unique=True, verbose_name='名称')
    image = models.ImageField(upload_to='banner', verbose_name='图片')
    link = models.CharField(max_length=64, verbose_name='跳转链接')
    info = models.TextField(verbose_name='详情')  # 也可以用详情表，宽高出处

    class Meta:
        db_table = 'luffy_banner'  # 重写表名
        verbose_name_plural = '轮播图表'  # admin中显示中文

    def __str__(self):
        return self.title