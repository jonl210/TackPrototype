from django.db import models

from datetime import datetime

#Group model
class Group(models.Model):
    name = models.CharField(max_length=500)
    u_id = models.CharField(max_length=8, default=0)
    date = models.DateTimeField(default=datetime.now)
