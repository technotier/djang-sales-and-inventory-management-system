from django.db import models

# Create your models here.
Department = (
    ("Accounts", "Accounts"),
    ("HR", "HR"),
    ("Sales", "Sales"),
    ("Marketing", "Marketing"),
    ("IT and Admin", "IT and Admin"),
    ("Business Development", "Business Development"),
)
class Employee(models.Model):
    full_name = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True, unique=True)
    email = models.EmailField(unique=True, blank=True, null=True, max_length=150)
    department = models.CharField(max_length=250, choices=Department)
    salary = models.IntegerField(blank=True, null=True)
    joining_date = models.DateField()
    img = models.ImageField(upload_to="employees/")
    
    def __str__(self) -> str:
        return self.full_name
    
