from django.urls import path
from .views import *

urlpatterns = [
    path('', get_all_users, name = 'users'),
    path('create', create_user, name = 'create_user'),
    path('edit/<id>', edit_user, name = 'edit_user'),
    path('delete/<id>', delete_user, name = 'delete_user'),
]