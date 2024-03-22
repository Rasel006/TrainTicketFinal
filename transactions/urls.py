from django.urls import path 
from .views import DepositeView

urlpatterns = [
    path("deposite/", DepositeView.as_view(), name='deposite'),
]