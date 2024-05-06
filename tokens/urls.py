from django.urls import path, include
from . import views

urlpatterns = [
    path('user/', views.UserList.as_view(), name='get_users'),
    path('user/<int:pk>/', views.UserDetail.as_view(), name='get_user'),


]
