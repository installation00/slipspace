# Generated by Django 4.1.3 on 2023-04-17 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('race_stats', '0003_alter_constructor_standings_points_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='constructor_results',
            name='points',
            field=models.FloatField(blank=True, null=True),
        ),
    ]