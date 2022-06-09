from django.db import models

# Create your models here.
class ProdectDetails(models.Model):
    product_name=models.CharField(max_length=255)
    description=models.TextField()
    quantity=models.IntegerField()
    Price=models.IntegerField()
