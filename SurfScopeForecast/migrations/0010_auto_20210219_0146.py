# Generated by Django 3.1.6 on 2021-02-19 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SurfScopeForecast', '0009_auto_20210219_0127'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='surfingInfo',
            name='secretList',
        ),
        migrations.AddField(
            model_name='surfinginfo',
            name='secretList',
            field=models.JSONField(default='{}'),
        ),
    ]
