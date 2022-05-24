from django.db import models

# Create your models here.
class StudentRegister(models.Model):
    name=models.CharField(max_length=30)
    contact=models.BigIntegerField() 
    email=models.CharField(max_length=30)
    username=models.CharField(max_length=40)
    password=models.CharField(max_length=40)
    
    class Meta:
        db_table="add_student"