# Generated by Django 3.0.5 on 2021-03-12 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SurfScopeForecast', '0002_surfinginfo_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='surfinginfo',
            name='secretList',
            field=models.TextField(default='{}'),
        ),
    ]