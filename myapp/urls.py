from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('simple', views.simple, name='simple'),
    path('contact', views.contact, name='contact'),
    path('delete/<int:id>/', views.delete),
]
