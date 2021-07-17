from django.contrib import admin

# Register your models here.
from .models import *

@admin.register(BidProduct)
class AdminBid(admin.ModelAdmin):
    list_display = ['product_name', 'current_bid', 'description', 'uploaded_by', 'uploaded_price', 'product_image', 'category']
    list_filter = ['category', 'current_bid', 'uploaded_price']
    #prepopulated_fields = {'current_bid': ['uploaded_price']}
    ordering = ['-upload_time']