from django.urls import path 
from .views import dashboard, users_all, borrowed_list

urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),
    path('users/', users_all, name='users'),
    path('borrowed/', borrowed_list, name='borrowed'),
]