from django.contrib import admin
from django.urls import path, include
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index), # http://127.0.0.1:8000/
    path('first/', include('myapp.urls')), # http://127.0.0.1:8000/first
    path('home/', include('myapp.urls')), # http://127.0.0.1:8000/home
]
