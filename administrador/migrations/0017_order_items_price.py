# Generated by Django 4.0.3 on 2022-04-15 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0016_remove_orders_unable_alter_order_items_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order_items',
            name='price',
            field=models.FloatField(),
            preserve_default=False,
        ),
    ]
