# Generated by Django 5.0.6 on 2024-06-02 18:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0023_alter_refunditem_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='transaction_id',
        ),
    ]
