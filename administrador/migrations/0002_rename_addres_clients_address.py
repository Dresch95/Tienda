# Generated by Django 4.0.3 on 2022-04-07 10:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='clients',
            old_name='addres',
            new_name='address',
        ),
    ]
