# Generated by Django 4.0.3 on 2022-04-11 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0013_alter_products_details_weight'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products_details',
            name='weight',
            field=models.FloatField(max_length=100, null=True),
        ),
    ]
