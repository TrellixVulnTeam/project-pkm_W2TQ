# Generated by Django 2.0.3 on 2018-04-23 10:36

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pkm_app', '0003_auto_20180420_1611'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='setupuser',
            name='emails_for_help',
        ),
        migrations.AddField(
            model_name='setupuser',
            name='emails_for_help',
            field=multiselectfield.db.fields.MultiSelectField(max_length=5000, null=True),
        ),
    ]
