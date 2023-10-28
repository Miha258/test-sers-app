from django.urls import path
from .views import *

urlpatterns = [
    path('', get_all_groups, name = 'groups'),
    path('create', create_group, name = 'create_group'),
    # path('edit/<id>', edit_group, name = 'edit_user'),
    # path('delete/<id>', delete_group, name = 'delete_user'),
]