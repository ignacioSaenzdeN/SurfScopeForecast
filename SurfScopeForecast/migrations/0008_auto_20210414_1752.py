# Generated by Django 3.1.7 on 2021-04-15 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SurfScopeForecast', '0007_auto_20210414_0234'),
    ]

    operations = [
        migrations.AddField(
            model_name='usersurdboard',
            name='imageUrl',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='usersurdboard',
            name='producstUrl',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='userwetsuit',
            name='imageUrl',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='userwetsuit',
            name='productUrl',
            field=models.TextField(default=''),
        ),
    ]
