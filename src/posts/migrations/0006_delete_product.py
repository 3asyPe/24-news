# Generated by Django 3.2 on 2021-04-22 16:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_alter_product_price'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Product',
        ),
    ]
