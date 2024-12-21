from django.db import models

# Create your models here.

class Country(models.Model):
    cname=models.CharField(max_length=100) 
    country_id=models.IntegerField(primary_key=True)

class Capital(models.Model):
    country_id=models.ForeignKey(Country,on_delete=models.CASCADE)
    cp_name=models.CharField(max_length=100)
    cpital_id=models.IntegerField()
