from django.db import models

# Create your models here.
class Member(models.Model):
    first_name= models.CharField(max_length=30)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField()
    gender = models.CharField(max_length=1)
    email = models.EmailField(max_length=20)
    preferr_number = models.IntegerField()
    preferr_colo = models.CharField(max_length=10)