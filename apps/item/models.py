from django.db import models
from datetime import datetime


class Item(models.Model):
    title = models.CharField(max_length=255)
    summary = models.CharField(max_length=1024, blank=True)
    content_url = models.CharField(max_length=255, blank=True)
    image_url = models.URLField(max_length=2000, blank=True)
    description = models.TextField()
    slug = models.SlugField(max_length=80, blank=True)

    published_at = models.DateField(default=datetime.now)
    created_at = models.DateTimeField(default=datetime.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
