# Generated by Django 3.2.11 on 2024-05-25 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='discount',
            field=models.FloatField(default=0, max_length=100, null=True),
        ),
    ]
