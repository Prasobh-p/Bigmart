from django.db import models
# Create your models here.


class ContactDB(models.Model):
    Name=models.CharField(max_length=500,null=True,blank=True)
    Email=models.EmailField(max_length=500,null=True,blank=True)
    Subject=models.CharField(max_length=1000,null=True,blank=True)
    Phone=models.IntegerField(null=True,blank=True)
    Message=models.CharField(max_length=1000,null=True,blank=True)

class RegisterDB(models.Model):
    Name = models.CharField(max_length=500, null=True, blank=True)
    Email = models.EmailField(max_length=500, null=True, blank=True)
    Password=models.CharField(max_length=500, null=True, blank=True)
    Confirmpassword=models.CharField(max_length=500, null=True, blank=True)

class cartDB(models.Model):
    Uname = models.CharField(max_length=500, null=True, blank=True)
    Pname = models.CharField(max_length=500, null=True, blank=True)
    Quantity = models.IntegerField(null=True,blank=True)
    Totalprice = models.IntegerField(null=True,blank=True)
