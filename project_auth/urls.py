"""
URL configuration for project_auth project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from rest_framework import routers
from app_auth.views import *

router = routers.DefaultRouter()

router.register(r'authors', AuthorViewSet)
router.register(r'books', BookViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('profile/', get_profile),
    path('token/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view(), name = 'token_refresh'),
    path('create-user/', create_user),
    # path('create-author/', create_author),
    path('create-book/', create_book),
    path('add-reader/', add_reader),
    path('remove-reader/', remove_reader),
    path('delete-book/', delete_book),
    path('', include(router.urls)),
]