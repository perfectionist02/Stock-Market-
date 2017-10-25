from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

## This contains the main database schema
class Stock(models.Model):
    symbol = models.CharField(max_length = 4, primary_key = True)
    current_price = models.FloatField()
    close_price = models.FloatField()
    open_price = models.FloatField()
    high_price = models.FloatField()
    low_price = models.FloatField()
    volume = models.IntegerField()
    
    def __str__(self):
        return self.symbol
        
        
        
class Customers(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.IntegerField()
    
    def buy(self,symbol,volume):
        stock=Stock.objects.get(symbol=symbol)
        if self.balance>(stock.current_price*volume) and stock.volume>volume:
            self.balance-=(stock.current_price*volume)
            stock.current_price+=(0.01*stock.current_price*volume)
            stock.volume-=volume
            isportfolio = Portfolio.objects.filter(stock__symbol=symbol).filter(owner__id=self.id).exists() 
            if isportfolio:
                portfolio = Portfolio.objects.get(stock__symbol=symbol,owner__id=self.id)
                portfolio.volume=portfolio.volume+volume
                portfolio.save()
            else:
                portfolio = Portfolio(owner=self,stock=stock,volume=volume)
                portfolio.save()
            stock.save()
            self.save()
            return True
        else:
            return False
            
            
            
    def sell(self,symbol,volume):
        stock=Stock.objects.get(symbol=symbol)
        isportfolio = Portfolio.objects.filter(stock__symbol=symbol).filter(owner__id=self.id).exists()
        if stock.current_price>(0.01*stock.current_price*volume) and isportfolio:
            self.balance+=(stock.current_price*volume)
            stock.current_price-=(0.01*stock.current_price*volume)
            stock.volume+=volume
            portfolio = Portfolio.objects.get(stock__symbol=symbol,owner__id=self.id)
            portfolio.volume-=volume
            if portfolio.volume<=0:
                portfolio.delete()
            portfolio.save()
            stock.save()
            self.save()
            return True
        else:
            return False
            
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Customers.objects.create(user=instance,balance=5000)

class Portfolio(models.Model):
    owner = models.ForeignKey(Customers, on_delete = models.CASCADE)
    stock = models.ForeignKey(Stock, on_delete = models.CASCADE)
    volume = models.IntegerField()


