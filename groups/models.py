from django.db import models

class Groups(models.Model):
    name = models.CharField(null = False, max_length = 200)
    description = models.CharField(null = False, max_length = 2000)
    data_analitics = models.BooleanField(null = False, default = False)
    service_analitics = models.IntegerField(null = False)
    voice_analitics = models.BooleanField(null = False, default = False)
    queue_status = models.BooleanField(null = False, default = False)
    voice_status = models.BooleanField(null = False, default = False)
    video = models.BooleanField(null = False, default = False)
    smart_access = models.BooleanField(null = False, default = False)
    diagrams = models.BooleanField(null = False, default = False)