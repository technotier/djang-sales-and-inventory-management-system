# Generated by Django 5.1 on 2024-09-02 15:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
        ('product', '0002_alter_product_name'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Invoice',
            new_name='Order',
        ),
    ]