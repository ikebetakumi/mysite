from django import forms
from .models import Category

class InquiryForm(forms.Form):
  # CATEGORY_CHOICES = Category.objects.order_by('sort').values_list('id', 'name')
  CATEGORY_CHOICES = (('',''),)

  name = forms.CharField(
        label='お名前',
        max_length=50,
        required=True,
        widget=forms.TextInput()
  )
  categoryname = forms.ChoiceField(
        label='カテゴリ',
        widget=forms.Select,
        choices=CATEGORY_CHOICES,
        required=True,
  )
  body = forms.CharField(
        label='お問い合わせ内容',
        required=True,
        widget=forms.Textarea()
  )
  email = forms.EmailField(
        label='メールアドレス',
        max_length=100,
        required=True,
        widget=forms.TextInput()
  )
  tel = forms.CharField(
        label='ご連絡先',
        max_length=11,
        required=False,
        widget=forms.TextInput()
  )
