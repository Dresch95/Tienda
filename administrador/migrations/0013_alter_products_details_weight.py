# Generated by Django 4.0.3 on 2022-04-11 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0012_alter_products_details_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products_details',
            name='weight',
            field=models.FloatField(blank=True, max_length=100),
        ),
    ]
