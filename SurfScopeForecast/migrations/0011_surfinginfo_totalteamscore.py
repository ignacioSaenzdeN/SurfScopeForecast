# Generated by Django 3.1.7 on 2021-04-29 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SurfScopeForecast', '0010_auto_20210415_0332'),
    ]

    operations = [
        migrations.AddField(
            model_name='surfinginfo',
            name='totalTeamScore',
            field=models.TextField(default='0'),
        ),
    ]
