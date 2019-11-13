from django.db import models

# Create your models here.
class Customer_Account(models.Model):
    idno=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=30)
    balance=models.DecimalField(max_digits=10,decimal_places=2)
    password=models.CharField(max_length=30)




# python manage.py makemigrations ['To create table']

# python manage.py makemigrate     ['To create database']