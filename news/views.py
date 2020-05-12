from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from mylibs.modules import lib_views
from .models import News
from .models import getNewsList, getNews
# from .models import Inquiry
# from .models import Category
# from .forms import InquiryForm
# from mylibs.modules import lib_forms
# from mylibs.modules import lib_mail


def index(request):
    assign_data = lib_views.getAssignData(request, {
        'breadcrumbList': {
            'TOP':{
                'label': 'トップページ',
                'urlname' : 'top'
            },
            'News':{
                'label': 'News',
            },
        },
        'news': getNewsList()
    })
    return render(request, 'news/index.html', assign_data)


def detail(request, id):
    detail = getNews(id)
    if detail == False:
        raise Http404
    newsList = getNewsList()
    prev = False
    next = False
    i = 0
    for values in newsList:
        if values['id'] == id:
            if i > 0:
                prev = newsList[i-1]
            if i < len(newsList)-1: 
                next = newsList[i+1]
            break
        i += 1
    assign_data = lib_views.getAssignData(request, {
        'breadcrumbList': {
            'TOP':{
                'label': 'トップページ',
                'urlname' : 'top'
            },
            'News':{
                'label': 'News',
                'urlname' : 'news'
            },
            'NewsDetail':{
                'label': values['title']
            },
        },
        'detail': detail,
        'next': next,
        'prev': prev,
        'list': newsList
    })
    return render(request, 'news/detail.html', assign_data)