from django.http import HttpResponse
from django.shortcuts import render
from mylibs.modules import lib_views
from django.urls import reverse
from news.models import getNewsList


def index(request):
    news = getNewsList(limit=5)
    assign_data = lib_views.getAssignData(request, {
        'breadcrumbList': {
            'TOP':{
                'label': 'トップページ'
            },
        },
        'news': news
    })
    return render(request, 'index.html', assign_data)