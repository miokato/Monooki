# Generated by Django 2.0.3 on 2018-03-21 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='pub_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
