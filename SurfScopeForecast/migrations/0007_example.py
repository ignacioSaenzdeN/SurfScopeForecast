# Generated by Django 3.1.6 on 2021-02-19 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SurfScopeForecast', '0006_auto_20210218_0146'),
    ]

    operations = [
        migrations.CreateModel(
            name='Example',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.JSONField()),
            ],
        ),
    ]
