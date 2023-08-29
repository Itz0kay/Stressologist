from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Program(models.Model):
    name = models.CharField(max_length=100, default='default text')
    desc = models.TextField( null=True, default='default text')
    link = models.TextField( null=True, default='default text')
    category = models.TextField( null=True, default='default text')
    duration = models.IntegerField( null=True, default=0)
    agegroup = models.IntegerField( null=True, default=0)
    level = models.IntegerField( null=True, default=0)
    photo = models.ImageField(upload_to="Images", null=True, default=None)

class ProgramLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    number = models.IntegerField(default=1)
    start_date = models.DateField(auto_now_add=True, blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)

