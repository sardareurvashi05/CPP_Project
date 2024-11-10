# Generated by Django 5.1.2 on 2024-11-09 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_alter_order_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='discount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
        migrations.AddField(
            model_name='product',
            name='reorder_threshold',
            field=models.PositiveIntegerField(default=10),
        ),
    ]
