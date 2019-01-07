from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=30)
    price = models.DecimalField(decimal_places=2, max_digits=8)
    description = models.TextField(blank=True, null=True)
    summary = models.TextField(blank=False, null=False)
    featured = models.BooleanField(default=False) #null=True or default=...
