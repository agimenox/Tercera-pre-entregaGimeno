from django.urls import path
from . import views

urlpatterns = [

    path('list_users/', views.list_users, name='list_users'),
    path('home_page/', views.home_page, name='home_page'),
    path('under_construction/', views.under_construction, name='under_construction'),
    path('list_clients/', views.list_clients, name='list_clients'),
    path('list_groups/', views.list_groups, name='list_groups'),
    
]