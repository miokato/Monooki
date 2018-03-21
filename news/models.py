from django.db import models


class News(models.Model):
    title = models.CharField(max_length=255)
    url = models.URLField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
