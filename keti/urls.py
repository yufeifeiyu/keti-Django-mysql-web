"""keti URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path
from myketi.views import *
urlpatterns = [
    path('', login),
    path('regist/', regist),
    path('login/', login),
    path(r'shenbao/', shenbao),
    path('edit_shenbao', edit_shenbao),
    path('edit_shenpi', edit_shenpi),
    path('home/', login),
    path('shenpi/', shenpi),
    path('myshenbao', myshenbao),
    path('myshenpi', myshenpi),
    path('review', review),
    path('user', user),
    path('del_test', del_test),
    path('edit_user', edit_user),
    path('del_user', del_user),
    path('add_user', add_user),
    path('project', project),
    path(r'download/<str:a>/<str:b>/<str:c>/<str:d>/', download),
    path(r'del_shenbao/<str:nid>/', del_shenbao),
    path(r'shenhe/<str:name>/<str:type>/<str:text>/<str:select>/', shenhe),

]
