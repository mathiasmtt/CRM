from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='seguridad_index'),
    path('user_list/', views.user_list, name='user_list'),
    path('edit_user_groups/<int:user_id>/', views.edit_user_groups, name='edit_user_groups'),
    path('delete_user/<int:user_id>/', views.delete_user, name='delete_user'),
]
