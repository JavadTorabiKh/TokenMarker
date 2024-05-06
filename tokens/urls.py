from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.get_users, name='get_users'),

]
