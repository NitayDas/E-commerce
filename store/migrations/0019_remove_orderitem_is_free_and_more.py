# Generated by Django 5.0.6 on 2024-06-01 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0018_orderitem_related_order_item'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='is_free',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='related_order_item',
        ),
        migrations.AddField(
            model_name='orderitem',
            name='free_items',
            field=models.IntegerField(default=0),
        ),
    ]
