from django.http import HttpResponse
from django.shortcuts import render
from mylibs.modules import lib_views
from django.urls import reverse
from news.models import getNewsList


def index(request):
    news = getNewsList(limit=5)
    # html = 'Hello Django.'
    # html += '参考文献：<a href="https://docs.djangoproject.com/ja/3.0/">https://docs.djangoproject.com/ja/3.0/</a><br>'
    # html += '<a href="https://qiita.com/d9magai/items/71dfa9ff95f7b70486a7">https://qiita.com/d9magai/items/71dfa9ff95f7b70486a7</a><br>'
    # html += '<br>DBのテーブルデータ消す：python manage.py flush'
    # return HttpResponse(html)
    assign_data = lib_views.getAssignData(request, {
        'breadcrumbList': {
            'TOP':{
                'label': 'トップページ'
            },
        },
        'news': news
    })
    return render(request, 'index.html', assign_data)
