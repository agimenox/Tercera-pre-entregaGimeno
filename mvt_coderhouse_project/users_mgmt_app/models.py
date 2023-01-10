from django.db import models

# Create your models here.
class Member(models.Model):
    first_name= models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField(null=True)
    gender = models.CharField(max_length=1)
    email = models.EmailField(max_length=20,null=True)
    preferr_number = models.IntegerField(null=True)
    preferr_color = models.CharField(max_length=10,null=True)

    def __str__(self) -> str:
        return f"{self.first_name}, {self.last_name}"

class Client(models.Model):
    client_name = models.CharField(max_length=100)
    client_email = models.CharField(max_length=100)
    client_phone = models.CharField(max_length=100)
    pass

class Group(models.Model):
    group_name = models.CharField(max_length=50)
    group_description = models.CharField(max_length=200)
    foreing_key = models.CharField(max_length=1)
    pass

