from django.urls import path, include
from . import views
from .views import create_post, ItemCreateView, login
from django.contrib.auth import views as auth_views

app_name = 'lang'

urlpatterns = [
    # path('', views.home, name='home'),
    path('', views.item, name='index'),
    path('items/', views.items, name='items'),
    path('items/add', ItemCreateView.as_view(), name='items_add'),
    path('test_page/', views.test_page, name='test_page'),
    # path('accounts/', include('allauth.urls')),
    path('login/', login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='lang/logout.html'), name='logout'),
]