# Generated by Django 5.0.1 on 2024-02-03 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matches', '0007_delete_stats'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='match_id',
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
    ]
