from django.db import models
from django.contrib.auth.models import User

class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    timestamp = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.image.name

class Result(models.Model):
    stresslevel = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ForeignKey('Image', on_delete=models.CASCADE)

    cwhen = models.DateField(auto_now_add=True, blank=True, null=True)
