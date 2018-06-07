# Generated by Django 2.0.3 on 2018-04-23 12:11

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pkm_app', '0004_auto_20180423_1606'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='setupuser',
            name='emails_for_help',
        ),
        migrations.AddField(
            model_name='setupuser',
            name='emails_for_help',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
