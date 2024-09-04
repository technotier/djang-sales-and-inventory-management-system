from django.db import models

# Create your models here.
INCOME_TYPE = (
    ("Product Sales", "Product Sales"),
    ("Rent", "Rent"),
    ("Other Income", "Other Income"),
)
class Income(models.Model):
    from_date = models.DateField(blank=True, null=True)
    to_date = models.DateField(blank=True, null=True)
    
    date = models.DateField(blank=True, null=True)
    income_type = models.CharField(max_length=100, choices=INCOME_TYPE, default="Product Sales")
    total_invoice = models.IntegerField(blank=True, null=True)
    amount = models.DecimalField(decimal_places=2, max_digits=20, blank=True, null=True)

