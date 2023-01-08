from django.urls import path
from . import views

urlpatterns = [

    path('list_users/', views.list_users, name='list_users'),
    path('home_page/', views.home_page, name='home_page'),
]