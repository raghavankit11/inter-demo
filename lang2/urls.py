from django.urls import path

from . import views

app_name = 'lang2'

urlpatterns = [
    path('', views.main, name='main'),

]