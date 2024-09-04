from django import forms
from .models import Income

class IncomeForm(forms.ModelForm):
    class Meta:
        model = Income
        fields = "__all__"
        widgets = {
            "date": forms.DateInput(attrs={"type": "date"})
        }
        exclude = ["from_date", "to_date"]