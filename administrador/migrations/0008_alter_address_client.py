# Generated by Django 4.0.3 on 2022-04-11 06:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0007_alter_address_client'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='client',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='administrador.clients'),
        ),
    ]
