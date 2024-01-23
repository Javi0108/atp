# Generated by Django 5.0.1 on 2024-01-23 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LoaderModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matches', models.FileField(help_text='Archivo de partidos', upload_to='')),
                ('players', models.FileField(help_text='Archivo de jugadores', upload_to='')),
                ('stats', models.FileField(help_text='Archivo de datos', upload_to='')),
            ],
        ),
    ]
