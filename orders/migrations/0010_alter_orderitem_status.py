# Generated by Django 5.1.3 on 2024-12-01 13:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0009_alter_order_status_alter_orderitem_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='status',
            field=models.ForeignKey(default=6, limit_choices_to={'status_category': 'Услуга'}, on_delete=django.db.models.deletion.SET_DEFAULT, to='orders.status', verbose_name='Статус услуги'),
        ),
    ]