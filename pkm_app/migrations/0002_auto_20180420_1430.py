# Generated by Django 2.0.3 on 2018-04-20 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pkm_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='setupuser',
            name='job_level',
            field=models.CharField(choices=[('L1', 'Level 1'), ('L2', 'Level 2'), ('L3', 'Level 3'), ('L4', 'Level 4'), ('Newly Joined', 'Newly joined')], max_length=2),
        ),
    ]
