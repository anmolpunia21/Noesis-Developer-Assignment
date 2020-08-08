from django.db import models

class Contact(models.Model):
    first_name = models.CharField(max_length=40,blank=False)
    middle_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40,blank=False)
    email = models.EmailField()
    mobile_no = models.CharField(max_length=40)
    landline_no = models.CharField(max_length=40)
    notes = models.CharField(max_length=40)

class Login(models.Model):
    username = models.CharField(max_length=40,blank=False)
    password = models.CharField(max_length=40,blank=False)