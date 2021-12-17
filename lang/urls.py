from django.urls import path

from . import views
from .views import create_post, ItemCreateView

app_name = 'lang'

urlpatterns = [
    # path('', views.home, name='home'),
    path('', views.item, name='index'),
    path('items/', views.items, name='items'),
    path('items/add', ItemCreateView.as_view(), name='items_add'),
    path('test_page/', views.test_page, name='test_page'),

]