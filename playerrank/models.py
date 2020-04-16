from django.db import models

# Create your models here.
from django.db.models import Model
from django.utils import timezone


class playerrank(Model):
    client_name = models.CharField(verbose_name='客户端名称', max_length=100)
    fraction = models.IntegerField(verbose_name='分数', default=0)
    create_time = models.DateTimeField(verbose_name='创建时间', default=timezone.now)
    update_time = models.DateTimeField(verbose_name="更新时间", default=timezone.now)

    class Meta:
        db_table = 'playerrank'
        verbose_name = '玩家排名'
        verbose_name_plural = verbose_name
