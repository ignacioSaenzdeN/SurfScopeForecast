# Generated by Django 3.1.7 on 2021-04-08 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SurfScopeForecast', '0004_auto_20210312_0139'),
    ]

    operations = [
        migrations.CreateModel(
            name='Boardshorts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itemType', models.TextField(default='')),
                ('imageUrl', models.TextField(default='')),
                ('productUrl', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='Surfboards',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itemType', models.TextField(default='')),
                ('imageUrl', models.TextField(default='')),
                ('productUrl', models.TextField(default='')),
                ('dimensions', models.TextField(default='')),
                ('volume', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='Wetsuits',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itemType', models.TextField(default='')),
                ('imageUrl', models.TextField(default='')),
                ('productUrl', models.TextField(default='')),
                ('legs', models.TextField(default='')),
                ('thickness', models.TextField(default='')),
                ('zipperType', models.TextField(default='')),
            ],
        ),
        migrations.AlterField(
            model_name='surfinginfo',
            name='secretList',
            field=models.TextField(default=''),
        ),
    ]
