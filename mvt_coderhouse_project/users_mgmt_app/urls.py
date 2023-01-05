from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_all_users, name='show_all_users')
]