from django.db import models


class News(models.Model):
    title = models.CharField(max_length=255)
    url = models.URLField(max_length=255)
    pub_date = models.DateTimeField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
