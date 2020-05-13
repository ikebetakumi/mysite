from django.db import models
from django.db.models.functions import Cast, Substr
from django.contrib import admin
import datetime

class News(models.Model):
    title = models.CharField('タイトル', max_length=100)
    body = models.TextField('本文')
    start_date = models.DateTimeField('公開日時')
    end_date   = models.DateTimeField('公開終了日時')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = 'news' # 小文字でよい


def getNewsList(limit=9999):
    newsObjects = News.objects
    newsObjects = newsObjects.filter(start_date__lte=datetime.datetime.now(), end_date__gte=datetime.datetime.now())
    newsObjects = newsObjects.order_by('start_date','id')[:limit]
    newsObjects = newsObjects.annotate(publish_date=Substr(Cast('start_date', models.CharField()),1,10))
    return newsObjects.values('id', 'title', 'publish_date')


def getNews(id):
    newsObjects = News.objects
    newsObjects = newsObjects.filter(id=id)
    newsObjects = newsObjects.annotate(publish_date=Substr(Cast('start_date', models.CharField()),1,10))
    valuesList = newsObjects.values('id', 'title', 'body', 'publish_date')
    if len(valuesList) == 0:
        return False
    return valuesList[0]