from django.db import models
from django.db.models.base import Model

class COUNTRY(models.Model):
    name = models.CharField(max_length=100,blank=True)
    para1 = models.CharField(max_length=600,blank=True)
    para2 = models.CharField(max_length=600,blank=True)

    def __str__(self):
        return self.name