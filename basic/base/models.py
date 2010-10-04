from django.db import models
from django.forms import ModelForm
from django import forms
from django.contrib.admin.widgets import AdminDateWidget

class Person(models.Model):
    name = models.CharField(max_length=50)
    date = models.DateField()
    surname = models.CharField(max_length=50, null=True, blank=True)
    bio = models.CharField(max_length=50)
    contacts = models.CharField(max_length=50)
    
    def __unicode__(self):
        return "%s %s" % (self.name, self.surname) 
        
class Location(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name

class PersonForm(ModelForm):
    date = forms.DateField(widget=AdminDateWidget)
    class Meta:
        model = Person    
