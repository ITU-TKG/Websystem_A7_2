# Generated by Django 5.1.4 on 2025-01-27 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PredictionData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weather', models.IntegerField(choices=[(0, '晴れ'), (1, '曇り'), (2, '雨')])),
                ('road', models.IntegerField()),
                ('time', models.IntegerField()),
                ('package', models.IntegerField()),
            ],
        ),
    ]
