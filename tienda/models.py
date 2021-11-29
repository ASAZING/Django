from django.db import models
from django.utils import timezone

class Brand(models.Model):
    description = models.CharField(max_length=200)
    
    def __str__(self):
        return self.description

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=18, decimal_places=2)
    quantity = models.IntegerField(blank=True, null=True)
    brand = models.ForeignKey('Brand', on_delete=models.CASCADE)
    imagen = models.FileField(upload_to='static/img/products/')
    created_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.name


