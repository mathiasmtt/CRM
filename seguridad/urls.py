from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='seguridad_index'),
    path('user_list/', views.user_list, name='user_list'),
]
