# Generated by Django 3.2.3 on 2022-10-24 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0009_customer_transactions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='transactions',
            field=models.JSONField(default='', null=True),
        ),
    ]
