from django.db import models

# Create your models here.
class CloProduct(models.Model):
    name = models.CharField(max_length=225, null = True, blank = True)
    image = models.ImageField(upload_to='images/', null = True, blank = True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null = True, blank = True)
    stock = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name