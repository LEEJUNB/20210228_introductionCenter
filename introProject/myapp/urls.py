from django.urls import path, include
from myapp import views

urlpatterns = [
    path('', views.home),
    path('home', include('myapp.urls')), # 앱명칭(myapp).urls
]