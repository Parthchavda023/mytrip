from django.db import models

# Create your models here.
class signupModel(models.Model):
    created = models.DateTimeField(auto_now_add = True)

    firstname = models.CharField(max_length = 50)
    lastname = models.CharField(max_length = 50)
    username = models.EmailField()
    password = models.CharField(max_length = 50)
    state = models.CharField(max_length = 50)
    city = models.CharField(max_length = 50)
    number = models.BigIntegerField()

class tripModel(models.Model):
    created = models.DateTimeField(auto_now_add = True)

    firstname = models.CharField(max_length = 50)
    lastname = models.CharField(max_length = 50)
    email = models.EmailField()
    mobile = models.BigIntegerField()
    place = models.CharField(max_length = 50)
    time = models.CharField(max_length = 50)