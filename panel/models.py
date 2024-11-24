from django.db import models

# Create your models here.

class user(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30, null=False)
    last_name = models.CharField(max_length=30, null=False)
    mail = models.CharField(max_length=50, null=False)
    phone= models.IntegerField(null=False)
    born = models.DateField(null=True)
    register = models.DateTimeField(auto_now_add=True, null=True)
    class goal :
        db_table = 'user' 

