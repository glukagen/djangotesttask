from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50, null=True, blank=True)
    bio = models.CharField(max_length=50)
    contacts = models.CharField(max_length=50)
