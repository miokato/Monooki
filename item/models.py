from django.db import models
from datetime import datetime


class Item(models.Model):
    title = models.CharField(max_length=255)
    url = models.URLField(max_length=255)
    description = models.TextField()

    created_at = models.DateTimeField(default=datetime.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
