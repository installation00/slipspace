# Generated by Django 4.1.3 on 2023-04-17 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('race_stats', '0009_alter_lap_times_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='results',
            name='time',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]