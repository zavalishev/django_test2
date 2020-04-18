from django.urls import path, include, re_path
from . import views
from django.views.generic import ListView, DetailView
from news.models import Articles


urlpatterns = [

    path('', ListView.as_view(queryset=Articles.objects.all().order_by("-date")[:20], template_name="news/news.html")),
    re_path(r'^(?P<pk>\d+)$', DetailView.as_view(model=Articles, template_name="news/news_info.html")),
]
