# Generated by Django 2.0.3 on 2018-03-18 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0002_auto_20180318_1630'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='amount',
            field=models.IntegerField(default=1, verbose_name='チケット数量'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='price',
            field=models.IntegerField(verbose_name='チケット価格'),
        ),
    ]