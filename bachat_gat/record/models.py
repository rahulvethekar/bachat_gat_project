from django.db import models

# Create your models here.

class MonthName (models.Model):
    month = models.CharField(max_length=10)
    def __str__(self):
            return "%s" % (self.month)


class UserName(models.Model):
    name = models.CharField(max_length=15)
    mobile = models.CharField(max_length=15)
    def __str__(self):
        return "%s" % (self.name)



class UserDetails(models.Model):
    month = models.ForeignKey(MonthName,on_delete=models.CASCADE)
    username = models.ForeignKey(UserName,on_delete=models.CASCADE)
    saving = models.IntegerField(default=0)
    intrest = models.IntegerField(default=0)
    # loan = models.IntegerField(default=0)
    paidLoan = models.IntegerField(default=0) 
    borrowLoan = models.IntegerField(default=0)
    fine = models.IntegerField(default=0)

class Calculation(models.Model):
    totalAmount = models.IntegerField(default=0)
    availableAmount = models.IntegerField(default=0)




