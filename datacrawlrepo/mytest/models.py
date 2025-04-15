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