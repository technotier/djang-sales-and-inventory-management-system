from django import forms
from .models import Sales

class SalesForm(forms.ModelForm):
    class Meta:
        model = Sales
        fields = "__all__"
        widgets = {
            "date": forms.DateInput(attrs={"type": "date"})
        }
        exclude = ["from_date", "to_date", "due_payment", "sales_type"]