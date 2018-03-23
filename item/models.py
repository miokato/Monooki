from django.db import models
from datetime import datetime


class Item(models.Model):
    title = models.CharField(max_length=255)
    content_url = models.CharField(max_length=255, blank=True)
    image_url = models.URLField(max_length=2000, blank=True)
    description = models.TextField()

    created_at = models.DateTimeField(default=datetime.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
