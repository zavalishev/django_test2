from django.shortcuts import render
from django.http import HttpResponse


def news(response):
    return render(response, 'news/news.html')

# Create your views here.
