from django.conf.urls import url path

from . import views

urlspatterns = [
    path('',views.index, name='index'),
]
