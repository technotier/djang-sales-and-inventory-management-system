from django.db import models

# Create your models here.
PAYMENT_TYPE = (
    ("Cash", "Cash"),
    ("Bank", "Bank"),
    ("Mobile Banking", "Mobile Banking"),
)
PAYMENT_STATUS = (
    ("Paid", "Paid"),
    ("Pending", "Pending"),
)
class Sales(models.Model):
    from_date = models.DateField(blank=True, null=True)
    to_date = models.DateField(blank=True, null=True)
    
    date = models.DateField(blank=True, null=True)
    customer = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=12, blank=True, null=True)
    sales_type = models.CharField(max_length=100, blank=True, null=True, default="Product Sales")
    invoice_number = models.CharField(max_length=100, blank=True, null=True)
    invoice_total = models.DecimalField(decimal_places=2, max_digits=20, blank=True, null=True)
    payment_receive = models.DecimalField(decimal_places=2, max_digits=20, blank=True, null=True)
    due_payment = models.DecimalField(decimal_places=2, max_digits=20, blank=True, null=True)
    payment_status = models.CharField(max_length=100, choices=PAYMENT_STATUS)
    payment_type = models.CharField(max_length=100, choices=PAYMENT_TYPE)
    
    def __str__(self) -> str:
        return str(self.customer)
    
    class Meta:
        verbose_name_plural = "Sales"
    
    def save(self, *args, **kwargs):
        self.due_payment = self.invoice_total - self.payment_receive
        super(Sales, self).save(*args, **kwargs)

    
