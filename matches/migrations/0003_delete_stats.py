# Generated by Django 4.1.11 on 2024-02-03 13:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('matches', '0002_stats'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Stats',
        ),
    ]