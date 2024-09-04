from django import forms
from .models import Expense

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = "__all__"
        widgets = {
            "date": forms.DateInput(attrs={"type": "date"})
        }
        exclude = ["from_date", "to_date"]

