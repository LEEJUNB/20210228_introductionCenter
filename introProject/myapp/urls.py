from django.urls import path, include
from myapp import views

urlpatterns = [
    path('', views.home), # 주소 : http://127.0.0.1:8000/home | 특징 : views파일의 home함수와 연결
]