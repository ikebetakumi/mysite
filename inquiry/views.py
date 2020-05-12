from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from mylibs.modules import lib_views
from .models import Inquiry
from .models import Category
from .forms import InquiryForm
from mylibs.modules import lib_forms
from mylibs.modules import lib_mail


def index(request):
    assign_data = lib_views.getAssignData(request, {
        'breadcrumbList': {
            'TOP':{
                'label': 'トップページ',
                'urlname' : 'top'
            },
            'Inquiry':{
                'label': 'お問い合わせ',
            },
        },
        'form': InquiryForm(request.POST or None)
    })
    return render(request, 'inquiry/index.html', assign_data)


def confirm(request):
    form = InquiryForm(request.POST or None)
    if form.is_valid():
        categoryname = form.cleaned_data['categoryname']
        for a, b in form.fields['categoryname'].choices:
            if str(a) == form.cleaned_data['categoryname']:
                categoryname = b
        assign_data = lib_views.getAssignData(request, {
            'breadcrumbList': {
                'TOP':{
                    'label': 'トップページ',
                    'urlname' : 'top'
                },
                'Inquiry':{
                    'label': 'お問い合わせ',
                    'urlname' : 'inquiry'
                },
                'InquiryConfirm':{
                    'label': '確認'
                }
            },
            'form': form,
            'submit_token': lib_forms.get_submit_token(request),
            'categoryname': categoryname
        })
        return render(request, 'inquiry/confirm.html', assign_data)
    return index(request)


def complete(request):
    form = InquiryForm(request.POST or None)
    if form.is_valid():
        assign_data = lib_views.getAssignData(request, {
            'breadcrumbList': {
                'TOP':{
                    'label': 'トップページ',
                    'urlname' : 'top'
                },
                'Inquiry':{
                    'label': 'お問い合わせ',
                    'urlname' : 'inquiry'
                },
                'InquiryComplete':{
                    'label': '完了'
                }
            },
            'form': form
        })
        if lib_forms.exists_submit_token(request) == False:
            return render(request, 'inquiry/complete.html', assign_data)
        lib_forms.get_submit_token(request)
        inq = Inquiry()
        inq.name = form.cleaned_data['name']
        inq.tel = form.cleaned_data['tel']
        inq.email = form.cleaned_data['email']
        inq.categoryname = Category.objects.get(id=int(form.cleaned_data['categoryname']))
        inq.body = form.cleaned_data['body']
        inq.save(force_insert=True)
        inquiryMail(request, inq)
        return render(request, 'inquiry/complete.html', assign_data)
    return redirect('inquiry')


def inquiryMail(request, inq):
    c = Inquiry.objects.get(id=inq.pk)
    name = str(c.name)
    change_url = request.META['HTTP_HOST'] + reverse('admin:inquiry_inquiry_change', args=(c.id,))
    subject = "[bee]お問い合わせがありました。"
    body = []
    body.append(name + "様からお問い合わせがありました。")
    body.append("詳細は以下のURLよりご確認ください。")
    body.append("")
    body.append("[URL]")
    body.append(change_url)
    body.append("")
    body.append("")
    body.append("----------------------------------------------------------")
    body.append("test")
    body.append("----------------------------------------------------------")
    body.append("")
    lib_mail.send("beforeaftertakumi@gmail.com", subject, '\n'.join(body))
    subject = "[bee]お問い合わせを承りました。"
    body = []
    body.append("※このメールはシステムからの自動返信です。")
    body.append("")
    body.append(name + "様")
    body.append("")
    body.append("お世話になっております。")
    body.append("お問い合わせ頂きありがとうございました。")
    body.append("")
    body.append("下記の内容でお問い合わせを承りました。")
    body.append("担当者からご連絡致しますので今しばらくお待ちくださいませ。")
    body.append("")
    body.append("--- ◆ お問い合わせ内容 ◆ ---")
    body.append("[お名前]" + name)
    body.append("[カテゴリ]" + str(c.categoryname))
    body.append("[お問い合わせ内容]")
    body.append(str(c.body))
    body.append("[メールアドレス]" + str(c.email))
    body.append("[ご連絡先]" + str(c.tel))
    body.append("----------------------------")
    body.append("")
    body.append("")
    body.append("※本メールに心当たりのない場合や、ご不明な点がございましたら、")
    body.append("下記までご連絡くださいますようお願いいたします。")
    body.append("")
    body.append("-----------------------------------------------------")
    body.append("test")
    body.append("-----------------------------------------------------")
    body.append("")
    lib_mail.send(inq.email, subject, '\n'.join(body))
