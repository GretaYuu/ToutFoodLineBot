# 設定這個LINE Bot應用程式(APP)的連結網址
from django.urls import path
from foodlinebot import views
 
urlpatterns = [
    path('callback', views.callback)
]

