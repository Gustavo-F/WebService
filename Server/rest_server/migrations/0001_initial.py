# Generated by Django 3.2.9 on 2021-11-06 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MeteorologicalStatistics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('hour', models.TimeField()),
                ('weather', models.CharField(max_length=100)),
                ('temperature', models.DecimalField(decimal_places=1, max_digits=3)),
            ],
        ),
    ]
