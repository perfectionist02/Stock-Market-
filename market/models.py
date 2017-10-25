from django.db import models
from django.conf import settings
## This contains the main 
class Stock(models.Model):
    symbol = models.CharField(max_length = 4, primary_key = True)
    current_price = models.IntegerField()
    close_price = models.IntegerField()
    open_price = models.IntegerField()
    high_price = models.IntegerField()
    low_price = models.IntegerField()
    volume = models.IntegerField()
    owner = models.ManyToManyField(settings.AUTH_USER_MODEL, through = 'Portfolio')
    
    def __str__(self):
        return self.symbol
        
class Portfolio(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    stock = models.ForeignKey(Stock, on_delete = models.CASCADE)
    volume = models.IntegerField()
    boughtat = models.IntegerField()
    
# Create your models here.