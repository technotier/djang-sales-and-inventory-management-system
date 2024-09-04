from django.db import models
from product.models import Product

# Create your models here.
class Order(models.Model):
    from_date = models.DateField(blank=True, null=True)
    to_date = models.DateField(blank=True, null=True)
    
    date = models.DateField(auto_now_add=True)
    customer = models.CharField("Customer Name", max_length=100, blank=True, null=True)
    phone = models.CharField("Phone Number", max_length=12, blank=True, null=True)
    
    line_one_product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="Product_1", blank=True, null=True)
    line_one_qty = models.IntegerField("Qty", blank=True, null=True, default=0)
    line_one_price = models.IntegerField("Price", blank=True, null=True, default=0)
    line_one_total_price = models.IntegerField("Total Price", blank=True, null=True)
    
    line_two_product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="Product_2", blank=True, null=True)
    line_two_qty = models.IntegerField("Qty", blank=True, null=True, default=0)
    line_two_price = models.IntegerField("Price", blank=True, null=True, default=0)
    line_two_total_price = models.IntegerField("Total Price", blank=True, null=True)
    
    line_three_product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="Product_3", blank=True, null=True)
    line_three_qty = models.IntegerField("Qty", blank=True, null=True, default=0)
    line_three_price = models.IntegerField("Price", blank=True, null=True, default=0)
    line_three_total_price = models.IntegerField("Total Price", blank=True, null=True)
    
    line_four_product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="Product_4", blank=True, null=True)
    line_four_qty = models.IntegerField("Qty", blank=True, null=True, default=0)
    line_four_price = models.IntegerField("Price", blank=True, null=True, default=0)
    line_four_total_price = models.IntegerField("Total Price", blank=True, null=True)
    
    line_five_product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="Product_5", blank=True, null=True)
    line_five_qty = models.IntegerField("Qty", blank=True, null=True, default=0)
    line_five_price = models.IntegerField("Price", blank=True, null=True, default=0)
    line_five_total_price = models.IntegerField("Total Price", blank=True, null=True)
    
    line_six_product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="Product_6", blank=True, null=True)
    line_six_qty = models.IntegerField("Qty", blank=True, null=True, default=0)
    line_six_price = models.IntegerField("Price", blank=True, null=True, default=0)
    line_six_total_price = models.IntegerField("Total Price", blank=True, null=True)
    
    line_seven_product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="Product_7", blank=True, null=True)
    line_seven_qty = models.IntegerField("Qty", blank=True, null=True, default=0)
    line_seven_price = models.IntegerField("Price", blank=True, null=True, default=0)
    line_seven_total_price = models.IntegerField("Total Price", blank=True, null=True)
    
    line_eight_product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="Product_8", blank=True, null=True)
    line_eight_qty = models.IntegerField("Qty", blank=True, null=True, default=0)
    line_eight_price = models.IntegerField("Price", blank=True, null=True, default=0)
    line_eight_total_price = models.IntegerField("Total Price", blank=True, null=True)
    
    line_nine_product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="Product_9", blank=True, null=True)
    line_nine_qty = models.IntegerField("Qty", blank=True, null=True, default=0)
    line_nine_price = models.IntegerField("Price", blank=True, null=True, default=0)
    line_nine_total_price = models.IntegerField("Total Price", blank=True, null=True)
    
    line_ten_product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="Product_10", blank=True, null=True)
    line_ten_qty = models.IntegerField("Qty", blank=True, null=True, default=0)
    line_ten_price = models.IntegerField("Price", blank=True, null=True, default=0)
    line_ten_total_price = models.IntegerField("Total Price", blank=True, null=True)
    
    total_amount = models.DecimalField("Invoice Total", decimal_places=2, max_digits=20, blank=True, null=True)
    
    def __str__(self) -> str:
        return str(self.customer)