from django.db import models

class Users(models.Model):
    username = models.CharField(null = False, max_length = 200)
    email = models.CharField(null = False, max_length = 200)
    group_id = models.IntegerField(null = False)
    is_admin = models.BooleanField(null = False, default = False)
    created_at = models.DateField(auto_now = True)