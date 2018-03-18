from django.db import models
from django.contrib.auth.models import User


class Event(models.Model):
    title = models.CharField('タイトル', max_length=255)
    description = models.TextField('イベント詳細')
    begin_date = models.DateTimeField('開始日時')
    end_date = models.DateTimeField('終了日時')
    place = models.CharField('開催場所', max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Ticket(models.Model):
    name = models.CharField('チケット名', max_length=255)
    event = models.ForeignKey('Event', on_delete=models.CASCADE, null=True)
    user = models.ManyToManyField(User, blank=True)
    price = models.IntegerField('チケット価格')
    amount = models.IntegerField('チケット数量', default=1)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
