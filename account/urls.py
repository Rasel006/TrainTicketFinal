from django.urls import path 
from .views import UserReg,UserLoginView,user_logout,editProfile,profileInfo,pass_change2

urlpatterns = [
    path('register/', UserReg.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', user_logout, name='logout'),
    path('info/', profileInfo, name='info'),
    path('profile/', editProfile, name='profile'),
    path('pass_change/', pass_change2, name='pass_change'),
]