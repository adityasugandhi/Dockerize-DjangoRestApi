from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200, blank=True, default='')
    brand_name = models.CharField(max_length=200, blank=True, default='')
    regular_price_value = models.IntegerField(default=0)
    offer_price_value = models.IntegerField(default=0)
    currency = models.CharField(max_length=10, blank=True, default='')
    classification_l1 = models.CharField(max_length=200, blank=True, default='')
    classification_l2 = models.CharField(max_length=200, blank=True, default='')
    classification_l3 = models.CharField(max_length=200, blank=True, default='')
    image_url = models.URLField(default=None)

    def __str__(self):
        return self.name