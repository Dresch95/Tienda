# Generated by Django 4.0.3 on 2022-04-08 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0003_alter_clients_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='size',
            field=models.CharField(default='AV', max_length=2, verbose_name=(('BG', 'BIG'), ('AV', 'AVERAGE'), ('SM', 'SMALL'))),
        ),
    ]