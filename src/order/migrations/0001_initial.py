# Generated by Django 5.1 on 2024-09-02 15:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0002_alter_product_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_date', models.DateField(blank=True, null=True)),
                ('to_date', models.DateField(blank=True, null=True)),
                ('date', models.DateField(auto_now_add=True)),
                ('customer', models.CharField(blank=True, max_length=100, null=True, verbose_name='Customer Name')),
                ('phone', models.CharField(blank=True, max_length=12, null=True, verbose_name='Phone Number')),
                ('line_one_qty', models.IntegerField(blank=True, default=0, null=True, verbose_name='Qty')),
                ('line_one_price', models.IntegerField(blank=True, default=0, null=True, verbose_name='Price')),
                ('line_one_total_price', models.IntegerField(blank=True, null=True, verbose_name='Total Price')),
                ('line_two_qty', models.IntegerField(blank=True, default=0, null=True, verbose_name='Qty')),
                ('line_two_price', models.IntegerField(blank=True, default=0, null=True, verbose_name='Price')),
                ('line_two_total_price', models.IntegerField(blank=True, null=True, verbose_name='Total Price')),
                ('line_three_qty', models.IntegerField(blank=True, default=0, null=True, verbose_name='Qty')),
                ('line_three_price', models.IntegerField(blank=True, default=0, null=True, verbose_name='Price')),
                ('line_three_total_price', models.IntegerField(blank=True, null=True, verbose_name='Total Price')),
                ('line_four_qty', models.IntegerField(blank=True, default=0, null=True, verbose_name='Qty')),
                ('line_four_price', models.IntegerField(blank=True, default=0, null=True, verbose_name='Price')),
                ('line_four_total_price', models.IntegerField(blank=True, null=True, verbose_name='Total Price')),
                ('line_five_qty', models.IntegerField(blank=True, default=0, null=True, verbose_name='Qty')),
                ('line_five_price', models.IntegerField(blank=True, default=0, null=True, verbose_name='Price')),
                ('line_five_total_price', models.IntegerField(blank=True, null=True, verbose_name='Total Price')),
                ('line_six_qty', models.IntegerField(blank=True, default=0, null=True, verbose_name='Qty')),
                ('line_six_price', models.IntegerField(blank=True, default=0, null=True, verbose_name='Price')),
                ('line_six_total_price', models.IntegerField(blank=True, null=True, verbose_name='Total Price')),
                ('line_seven_qty', models.IntegerField(blank=True, default=0, null=True, verbose_name='Qty')),
                ('line_seven_price', models.IntegerField(blank=True, default=0, null=True, verbose_name='Price')),
                ('line_seven_total_price', models.IntegerField(blank=True, null=True, verbose_name='Total Price')),
                ('line_eight_qty', models.IntegerField(blank=True, default=0, null=True, verbose_name='Qty')),
                ('line_eight_price', models.IntegerField(blank=True, default=0, null=True, verbose_name='Price')),
                ('line_eight_total_price', models.IntegerField(blank=True, null=True, verbose_name='Total Price')),
                ('line_nine_qty', models.IntegerField(blank=True, default=0, null=True, verbose_name='Qty')),
                ('line_nine_price', models.IntegerField(blank=True, default=0, null=True, verbose_name='Price')),
                ('line_nine_total_price', models.IntegerField(blank=True, null=True, verbose_name='Total Price')),
                ('line_ten_qty', models.IntegerField(blank=True, default=0, null=True, verbose_name='Qty')),
                ('line_ten_price', models.IntegerField(blank=True, default=0, null=True, verbose_name='Price')),
                ('line_ten_total_price', models.IntegerField(blank=True, null=True, verbose_name='Total Price')),
                ('total_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, verbose_name='Invoice Total')),
                ('line_eight_product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Product_8', to='product.product')),
                ('line_five_product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Product_5', to='product.product')),
                ('line_four_product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Product_4', to='product.product')),
                ('line_nine_product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Product_9', to='product.product')),
                ('line_one_product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Product_1', to='product.product')),
                ('line_seven_product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Product_7', to='product.product')),
                ('line_six_product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Product_6', to='product.product')),
                ('line_ten_product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Product_10', to='product.product')),
                ('line_three_product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Product_3', to='product.product')),
                ('line_two_product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Product_2', to='product.product')),
            ],
        ),
    ]
