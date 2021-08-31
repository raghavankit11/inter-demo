from django.urls import path

from . import views
from .views import create_post

app_name = 'lang'

urlpatterns = [
    # path('', views.home, name='home'),
    path('', views.item, name='index'),
    path('item/', views.item, name='item'),
    path('test_page/', views.test_page, name='test_page'),

]