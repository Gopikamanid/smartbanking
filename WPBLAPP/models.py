from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.db import migrations, models
import datetime
class Migration(migrations.Migration):

    dependencies = [
        ('WPBLAPP', '0001_initial'),  # Replace with the actual app name and the previous migration name
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]

class User(models.Model):
    num = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=10)
    totalamount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    date = models.DateField(default=datetime.date.today)
    year = models.IntegerField(blank=True, null=True)
    
    def __str__(self):
        return self.num

    # def save(self, *args, **kwargs):
    #     if self.date:
    #         self.year = self.date.year
    #     super().save(*args, **kwargs)

    

class Transaction(models.Model):
    userid=models.ForeignKey(User,on_delete=models.CASCADE)
    deposit=models.DecimalField(max_digits=10, decimal_places=2,null=True)
    withdraw=models.DecimalField(max_digits=10, decimal_places=2,null=True)
    date=models.DateField(auto_now_add=True)
    def __str__(self):
        return self.userid.name
class SADUser(models.Model):
    num=models.CharField(max_length=1000)
    name=models.CharField(max_length=100)
    phone=models.CharField(max_length=10)
    totalamount=models.DecimalField(max_digits=10, decimal_places=2,null=True, blank=True)
    date = models.DateField(default=datetime.date.today)
    
    def __str__(self):
        return self.num
    
    # def save(self, *args, **kwargs):
    #     if self.date:
    #         self.year = self.date.year
    #     super().save(*args, **kwargs)
    
class SADtransaction(models.Model):
    usernum=models.ForeignKey(SADUser,on_delete=models.CASCADE)
    deposit=models.DecimalField(max_digits=10, decimal_places=2,null=True)
    withdraw=models.DecimalField(max_digits=10, decimal_places=2,null=True)
    date=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.usernum.name