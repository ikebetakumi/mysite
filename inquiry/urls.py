from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='inquiry'),
    path('confirm/', views.confirm, name='inquiry_confirm'),
    path('complete/', views.complete, name='inquiry_complete'),
]