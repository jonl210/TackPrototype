from django.db import models

from datetime import datetime

#Group model
class Group(models.Model):
    name = models.CharField(max_length=500)
    date = models.DateTimeField(default=datetime.now)
