# Generated by Django 4.2.6 on 2023-10-15 11:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.RemoveField(
            model_name='product',
            name='stock_quantity',
        ),
    ]
