from django.db import migrations, models
from django.contrib import admin


class Category(models.Model):
    name = models.CharField('カテゴリ名',max_length=100)
    sort = models.IntegerField('並び順', default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'catgories' # 小文字でよい
				# verbose_name = 'ブログ'

class Inquiry(models.Model):
    name = models.CharField('名前',max_length=100)
    tel = models.CharField('連絡先',max_length=11)
    email = models.EmailField('Eメール')
    categoryname = models.ForeignKey(Category, on_delete=models.CASCADE, default=0, related_name="+")
    body = models.TextField('本文')
    reply = models.BooleanField('返信フラグ', default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'inquiries' # 小文字でよい

# class Blacklist(models.Model):
#     name  = models.CharField('name',max_length=100)
#     tel = models.CharField('tel',max_length=11)
#     email = models.EmailField('email')
#     title = models.CharField('title',max_length=100)
#     body = models.TextField('body')
#     reply = models.BooleanField(default=False)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.name