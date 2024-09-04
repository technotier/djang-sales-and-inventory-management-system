from django.db import models

# Create your models here.
PAYMRNT_TYPE = (
    ("Cash", "Cash"),
    ("Bank", "Bank"),
    ("Mobile Banking", "Mobile Banking"),
)
EXPENSE_TYPE = (
    ("Salary", "Salary"),
    ("Utility Bills", "Utility Bills"),
    ("Office Expense", "Office Expense"),
    ("Others", "Others"),
)

class Expense(models.Model):
    from_date = models.DateField(blank=True, null=True)
    to_date = models.DateField(blank=True, null=True)
    
    date = models.DateField(blank=True, null=True)
    expense_type = models.CharField(max_length=200, choices=EXPENSE_TYPE, default="Office Expense")
    paid_to = models.CharField(max_length=100, blank=True, null=True)
    expense_amount = models.DecimalField(decimal_places=2, max_digits=20, blank=True, null=True)
    payment_type = models.CharField(max_length=100, choices=PAYMRNT_TYPE, default="Cash")
    
    def __str__(self) -> str:
        return self.expense_type