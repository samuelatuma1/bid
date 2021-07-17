from django.db import models

from django.conf import settings
from django.db.models.expressions import OrderBy

# Create your models here.

class BidProduct(models.Model):
    CHOICES = [('fashion', 'fashion'), ('vehicles', 'vehicles'), ('others', 'others')]
    product_name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(max_length=100, choices=CHOICES)
    period_on_bid = models.DateTimeField(blank=True, null=True)
    upload_time = models.DateTimeField(auto_now_add=True, db_index=True)
    
    uploaded_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    uploaded_price = models.DecimalField(decimal_places=2, max_digits=10) 
    
    product_image = models.ImageField(upload_to='biduploads')
    current_bid = models.DecimalField(decimal_places=2, max_digits=10)
    
    class Meta:
        ordering = ['-upload_time']
        
    def __str__(self):
        return self.product_name