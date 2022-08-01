# 프로젝트명/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls), # admin path 지정
    path('', include('backend_dj.urls')), # backend_dj/urls.py 사용
]