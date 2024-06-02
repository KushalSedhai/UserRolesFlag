from django.db import models

# Create your models here.
class Listings(models.Model):
    class SaleType(models.TextChoices):
        FOR_SALE ='For Sale'
        FOR_RENT = 'For Rent'
        
    agent = models.CharField(max_length=244)
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    
    price = models.IntegerField()
    location = models.CharField(max_length=100)
    description = models.TextField()
    sale_type = models.CharField(max_length=100, choices=SaleType.choices, default=SaleType.FOR_SALE)
    