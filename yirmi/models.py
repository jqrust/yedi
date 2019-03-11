from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    is_activated = models.BooleanField(default=False)
    email = models.EmailField(unique=True)
    EMAIL_FIELD = 'email'
class Department(models.Model):
    name = models.CharField(max_length=128)
    user = models.ForeignKey(User,on_delete=models.PROTECT)
    def __str__(self):
        return self.name
class Report(models.Model):
    state_list = (
        ('C' , 'Created'),
        ('I' , 'In_progress'),
        ('S' , 'Success'),
        ('F' , 'Failed'),
        )
    date_created = models.DateTimeField(auto_now_add=True)
    date_seen = models.DateTimeField(null=True,blank=True)
    date_end = models.DateTimeField(null=True,blank=True)
    state = models.CharField(max_length=1, choices=state_list, default='C')
    header = models.CharField(max_length=128)
    text = models.TextField()
    createdby = models.ForeignKey(User,on_delete=models.CASCADE)
    department = models.ForeignKey(Department,on_delete=models.PROTECT)
