from django.urls import path
from . import views


urlpatterns = [
    path('add_train', views.Add_trainView.as_view(),name='add_train'),
    path('train_list', views.train_list,name='train_list'),
    path('edit_train/<int:id>', views.editTrainInfo,name='edit_train'),
    path('delete_train/<int:id>/', views.delete_train,name='delete_train'),
    path('details_train/<int:id>', views.Detail_train.as_view(), name='details_train'),
    path('buy/<int:train_id>', views.buyTicket, name='buy'),
]