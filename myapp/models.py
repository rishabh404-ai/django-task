from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    type_choices = (
        ('survey','survey'),
        ('discussion','discussion'),
        ('diary','diary')
    )
    title = models.CharField(max_length=200,null=True,blank=True)
    desc= models.CharField(max_length=200,null=True,blank=True) 
    task_type=models.CharField(choices=type_choices,max_length=10,null=True,blank=True) 
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    
class Tile(models.Model):
    status_choices = (
        ('live','live'),
        ('pending','pending'),
        ('archived','archived')
    )
    launch_date = models.DateField()
    status = models.CharField(choices=status_choices,max_length=10,null=True,blank=True) 
    tasks = models.ManyToManyField(to=Task)    