# Generated by Django 3.1.7 on 2021-04-08 17:59

from django.db import migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('SurfScopeForecast', '0005_auto_20210408_1059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='surfinginfo',
            name='secretList',
            field=jsonfield.fields.JSONField(default='{}'),
        ),
    ]
