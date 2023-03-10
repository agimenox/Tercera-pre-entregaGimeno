from django.urls import path
from . import views
from .views import GroupListView, GroupDetailView,GroupCreateView, GroupUpdateView, GroupDeleteView

urlpatterns = [

    path('list-users/', views.list_users, name='list_users'),
    path('home-page/', views.home_page, name='home_page'),
    path('under-construction/', views.under_construction, name='under_construction'),
    path('list-clients/', views.list_clients, name='list_clients'),
    path('list-groups/', views.list_groups, name='list_groups'),
    path('new-client/', views.new_client, name='new_client'),
    path('search-clients/', views.search_clients, name='search_clients'),
    path('new-group/', views.new_group, name='new_group'),
    path('search-group/', views.search_groups, name='search_groups'),
    path('new-user/', views.new_user, name='new_user'),
    path('search-user/', views.search_users, name='search_users'),
    path('show-user-data/<int:id>', views.show_user_data, name='show_user_data'),
    path('edit-user-data/<int:id>', views.edit_user_data, name='edit_user_data'),
    path('delete-user/<int:id>', views.delete_user, name='delete_user'),
    path('list-groups2/', GroupListView.as_view(), name="list_groups2"),
    path('detail-group2/<int:pk>/', GroupDetailView.as_view(), name="detail_group"),
    path('create-group2/', GroupCreateView.as_view(), name="create_group"),
    path('edit-group2/<int:pk>/', GroupUpdateView.as_view(), name="edit_group"),
    path('delete-group2/<int:pk>/', GroupDeleteView.as_view(), name="delete_group"),
         
]