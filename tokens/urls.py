from django.urls import path, include
from . import views

urlpatterns = [
    path('user/', views.UserList.as_view(), name='get_users'),
    path('user/<int:pk>/', views.UserDetail.as_view(), name='get_user'),

    path('token/', views.TokenList.as_view(), name='get_tokens'),
    path('token/<int:pk>/', views.TokenDetail.as_view(), name='get_token'),


]
