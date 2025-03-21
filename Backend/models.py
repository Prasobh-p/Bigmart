from django.db import models

# Create your models here.
class martdb(models.Model):
    Name=models.CharField(max_length=50,null=True,blank=True)
    Description=models.CharField(max_length=300,null=True,blank=True)
    Image=models.ImageField(upload_to="media",null=True,blank=True)

class prodb(models.Model):
    CatName=models.CharField(max_length=50,null=True,blank=True)
    Name=models.CharField(max_length=50,null=True,blank=True)
    Price=models.IntegerField(null=True,blank=True)
    Image=models.ImageField(upload_to="product images",null=True,blank=True)
    Description=models.CharField(max_length=300,null=True,blank=True)


