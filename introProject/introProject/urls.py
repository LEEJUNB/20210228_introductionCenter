from django.urls import path, include
from myapp import views

urlpatterns = [
    path('', views.index), # 주소 : http://127.0.0.1:8000/ | 특징 : index함수 연결
    # path('', include('myapp.urls')), # 주소 : http://127.0.0.1:8000/ | 특징 : urls 매핑 방식
    path('home/', include('myapp.urls')), # 주소 : http://127.0.0.1:8000/home | 특징 : myapp앱의 urls와 매핑
]
