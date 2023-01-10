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
    pass
