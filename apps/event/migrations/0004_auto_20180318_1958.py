# Generated by Django 2.0.3 on 2018-03-18 10:58

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('event', '0003_auto_20180318_1632'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='user',
        ),
        migrations.AddField(
            model_name='ticket',
            name='user',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
