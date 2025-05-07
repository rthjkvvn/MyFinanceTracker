from django.db import models
from django.contrib.auth.hashers import make_password

# Create your models here.

class User(models.Model):
    #uid = models.CharField(max_length=20)
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=150)
    password = models.CharField(max_length=100, null=True, blank=True)

    def set_password(self, raw):
        self.password=make_password(raw)
    
    class Meta:
        db_table = "user"

class Transaction(models.Model):
    tuname= models.CharField(max_length=100)
    tamount = models.IntegerField()
    tcategory= models.CharField(max_length=100)
    tdate= models.DateField()

    def __str__(self):
        return f"{self.tuname} - {self.tamount}"
    
from django.db import models



class Category1(models.Model):
    cname=models.CharField(max_length=150)
    cset_budget=models.IntegerField()
    cspend=models.IntegerField()
    cusername=models.CharField(max_length=150)

    class Meta:
        db_table = "category1"