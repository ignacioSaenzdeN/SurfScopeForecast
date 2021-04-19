# Generated by Django 3.1.7 on 2021-04-14 09:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SurfScopeForecast', '0006_auto_20210408_1059'),
    ]

    operations = [
        migrations.AddField(
            model_name='surfinginfo',
            name='boardSuggestion',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='surfinginfo',
            name='wetSuitSuggestion',
            field=models.TextField(blank=True),
        ),
        migrations.CreateModel(
            name='UserWetsuit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.TextField(default='')),
                ('size', models.TextField(default='')),
                ('waterTemp', models.TextField(default='')),
                ('coldSensitivy', models.TextField(default='')),
                ('zipperType', models.TextField(default='')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wetsuit', to='SurfScopeForecast.surfinginfo')),
            ],
        ),
        migrations.CreateModel(
            name='UserSurdboard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.TextField(default='')),
                ('height', models.TextField(default='')),
                ('size', models.TextField(default='')),
                ('level', models.TextField(default='')),
                ('waveSize', models.TextField(default='')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='surdboard', to='SurfScopeForecast.surfinginfo')),
            ],
        ),
    ]