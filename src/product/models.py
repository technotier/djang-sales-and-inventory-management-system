from django.db import models

# Create your models here.
PRODUCT_UNIT = (
    ("Pack", "Pack"),
    ("Pcs", "Pcs"),
    ("KG", "KG"),
    ("Ltr", "Ltr"),
)

class Product(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True, unique=True)
    features = models.CharField(max_length=500, blank=True, null=True)
    model = models.CharField(max_length=300, blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    unit = models.CharField(max_length=100, choices=PRODUCT_UNIT)
    in_stock = models.IntegerField(blank=True, null=True)
    img = models.ImageField(upload_to="prducts/")

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural = "All Product"


