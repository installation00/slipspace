# Generated by Django 4.1.3 on 2023-04-17 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('race_stats', '0002_alter_circuits_alt_alter_circuits_circuitid_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='constructor_standings',
            name='points',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='constructor_standings',
            name='positionText',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
