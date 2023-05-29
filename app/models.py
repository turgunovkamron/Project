from django.db import models


# Create your models here.

class Student(models.Model):
    ism = models.CharField(max_length=122)
    familya = models.CharField(max_length=123)
    sinf = models.CharField(max_length=125)
    yosh = models.CharField(max_length=124)

    def __str__(self):
        return f"{self.ism}  {self.familya}"
