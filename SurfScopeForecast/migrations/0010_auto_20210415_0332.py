# Generated by Django 3.1.7 on 2021-04-15 10:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SurfScopeForecast', '0009_auto_20210414_1918'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserSurfboard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.TextField(default='')),
                ('height', models.TextField(default='')),
                ('size', models.TextField(default='')),
                ('level', models.TextField(default='')),
                ('waveSize', models.TextField(default='')),
                ('imageUrl', models.TextField(default='')),
                ('productUrl', models.TextField(default='')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='surfboard', to='SurfScopeForecast.surfinginfo')),
            ],
        ),
        migrations.DeleteModel(
            name='UserSurdboard',
        ),
    ]
