# Generated by Django 3.2.8 on 2021-10-17 05:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pokemonUnite', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pokemon',
            name='image',
        ),
    ]
