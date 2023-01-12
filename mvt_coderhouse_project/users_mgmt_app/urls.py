from django.urls import path
from . import views

urlpatterns = [

    path('list-users/', views.list_users, name='list_users'),
    path('home-page/', views.home_page, name='home_page'),
    path('under-construction/', views.under_construction, name='under_construction'),
    path('list-clients/', views.list_clients, name='list_clients'),
    path('list-groups/', views.list_groups, name='list_groups'),
    path('new-client/', views.new_client, name='new_client'),
    
]