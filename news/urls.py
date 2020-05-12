from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='news'),
		path('<int:id>', views.detail, name="news_detail")
]