# Generated by Django 5.0.6 on 2024-06-01 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0014_refunditem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='refunditem',
            name='quantity',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
