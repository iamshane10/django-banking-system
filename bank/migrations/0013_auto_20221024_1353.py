# Generated by Django 3.2.3 on 2022-10-24 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0012_alter_customer_transactions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='phone',
            field=models.CharField(max_length=13),
        ),
        migrations.AlterField(
            model_name='customer',
            name='transactions',
            field=models.TextField(default='', null=True),
        ),
    ]
