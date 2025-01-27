from django.urls import path
from .views import data_input_view, data_list_view

urlpatterns = [
    path('input/', data_input_view, name='data_input'),
    path('list/', data_list_view, name='data_list'),
]