from django.db import models

class TableM(models.Model):
     ID= models.IntegerField
     ID1 = models.IntegerField
     Domain = models.CharField(max_length=1200,blank=True)
     Insight = models.CharField(max_length=1200,blank=True)
     Query = models.CharField(max_length=1200,blank=True)
     Recordcount = models.CharField(max_length=1200,blank=True)
     LastRefreshedOn = models.DateTimeField(blank=True)

#     def __str__(self):
#         return str(self.LastRefreshedOn)

     def _str_(self):
         return self.ID

'''
# Create your models here.
class FAMILY(models.Model):
    ID = models.IntegerField
    NAME = models.CharField(max_length=100)

    def _str_(self):
        return self.NAME

class Item(models.Model):
    family=models.ForeignKey(FAMILY,on_delete=models.CASCADE)
    text=models.CharField(max_length=300)
    complete=models.BooleanField()

    def _strt_(self):
        return self.text'''




