from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    is_supermarket = models.BooleanField(default=False)
    address = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.username


class Product(models.Model):
    name = models.CharField(max_length=100)
    picture = models.URLField(blank=True, null=True)
    unity = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class List(models.Model):
    user = models.ForeignKey("User",on_delete=models.CASCADE, related_name="lists")
    name = models.CharField(max_length=100)
    products = models.ManyToManyField(Product, blank=True)

    def __str__(self):
        return f"{self.name} ({self.user.username})"
    
class PriceMkt(models.Model):
    supermarket = models.ForeignKey("User", on_delete=models.CASCADE, limit_choices_to={'is_supermarket': True})
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"{self.product} - {self.supermarket} - {self.price}"