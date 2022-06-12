from django.db import models

# Create your models here.
class Item(models.Model):
    companyname=models.CharField(max_length=50, unique=True)
    code=models.IntegerField(unique=True)
    ceo=models.CharField(max_length=20)
    turnover=models.IntegerField()
    website=models.CharField(max_length=50)
    stockenlist=models.CharField(max_length=3)
class Price(models.Model):
    companyname=models.ForeignKey(Item,on_delete=models.CASCADE)
    sdate=models.DateTimeField(auto_now_add=True,null=True)
    price_stock=models.FloatField(default=0.00)

    def __str__(self):
        return self.companyname

