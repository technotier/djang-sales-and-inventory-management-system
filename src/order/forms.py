from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            "customer", "phone",
            "line_one_product", "line_one_qty", "line_one_price", "line_one_total_price",
            "line_two_product", "line_two_qty", "line_two_price", "line_two_total_price",
            "line_three_product", "line_three_qty", "line_three_price", "line_three_total_price",
            "line_four_product", "line_four_qty", "line_four_price", "line_four_total_price",
            "line_five_product", "line_five_qty", "line_five_price", "line_five_total_price",
            "line_six_product", "line_six_qty", "line_six_price", "line_six_total_price",
            "line_seven_product", "line_seven_qty", "line_seven_price", "line_seven_total_price",
            "line_eight_product", "line_eight_qty", "line_eight_price", "line_eight_total_price",
            "line_nine_product", "line_nine_qty", "line_nine_price", "line_nine_total_price",
            "line_ten_product", "line_ten_qty", "line_ten_price", "line_ten_total_price",
            "total_amount"
            ]

