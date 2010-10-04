from django.db import models
from django.forms import ModelForm

class Person(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50, null=True, blank=True)
    bio = models.CharField(max_length=50)
    contacts = models.CharField(max_length=50)

class Location(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name

class PersonForm(ModelForm):
    class Meta:
        model = Person    
