"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path, include, re_path

import lang
import lang2
from core import settings
from lang.views import update_timezone, create_post

urlpatterns = [
    path('admin/', admin.site.urls),
    path('update_timezone', update_timezone, name='update_timezone'),
    path('post/new', create_post, name='post-new'),

]

urlpatterns += i18n_patterns (
    path('', include('lang.urls', namespace='lang')),
    path('other/', include('lang2.urls', namespace='lang2')),

)

if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns += [
        re_path(r'^rosetta/', include('rosetta.urls'))
    ]