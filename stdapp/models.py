from django.db import models
from exapp.models import Exersise

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=255)

class CheckPoint(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    exersise = models.ForeignKey(Exersise,on_delete=models.PROTECT)
    status = models.BooleanField(default=False)
