# Generated by Django 4.1.3 on 2023-04-17 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('race_stats', '0007_alter_sprint_results_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pit_stops',
            name='duration',
            field=models.DurationField(blank=True, null=True),
        ),
    ]
