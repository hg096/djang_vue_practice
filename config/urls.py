"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# 앱이름/urls.py 생성

from django.urls import include, path
from rest_framework import routers  # router import
from backend_dj import views  # views.py import

router = routers.DefaultRouter()  # DefaultRouter 설정
router.register('user', views.UserViewSet)  # ViewSet과 함께 user라는 router 등록

urlpatterns = [
    path('', include(router.urls)),
]