from django.db import models

from datetime import datetime

#Post model
class Post(models.Model):
    u_id = models.CharField(max_length=11, default=0)
    url = models.URLField()
    description = models.TextField()
    date = models.DateTimeField(default=datetime.now)
