from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),  #http://������
    path('result', views.result, name="result"), #https://������/result
]