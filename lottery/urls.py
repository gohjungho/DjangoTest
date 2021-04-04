from django.urls import path
from . import views

urlpatterns = [
    path('', views.lottery_list, name='lottery_list'),
    path('lottery/<int:pk>/', views.lottery_detail, name='lottery_detail'),
]