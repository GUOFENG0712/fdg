from django.db import models

# Create your models here.
class MyModel(models.Model):
    '''
    河南彭于晏嘿嘿
    '''
    name = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.IntegerField()
    pass
class WcyDate(models.Model):
    '''
    篮球皇帝
    '''
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    hobby = models.CharField(max_length=100)
    pass