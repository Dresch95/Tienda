# Generated by Django 4.0.3 on 2022-04-08 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0004_alter_products_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='type',
            field=models.CharField(choices=[('SH', 'SHIPPING'), ('BL', 'BILLING'), ('FL', 'FULL')], default='FL', max_length=2),
        ),
        migrations.AlterField(
            model_name='products',
            name='size',
            field=models.CharField(choices=[('BG', 'BIG'), ('AV', 'AVERAGE'), ('SM', 'SMALL')], default='AV', max_length=2),
        ),
    ]