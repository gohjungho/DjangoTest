from django.urls import path
from . import views

urlpatterns = [
    path('', views.lottery_list, name='lottery_list'),
]