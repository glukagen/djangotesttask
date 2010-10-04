from django.db import models
from django.forms import ModelForm
from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from django.db.models.signals import post_save, pre_delete

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
    PRIORITY_CHOICES = (
        ('0', '1-choice'),
        ('l', '2-choice'),
    )
    priority = models.CharField(max_length=1, choices=PRIORITY_CHOICES)
    def __unicode__(self):
        return self.name

class PersonForm(ModelForm):
    date = forms.DateField(widget=AdminDateWidget)
    class Meta:
        model = Person
        
class Log(models.Model):
    OBJECT_CHOICES = (
        ('p', 'Person'),
        ('l', 'Location'),
    )
    object = models.CharField(max_length=1, choices=OBJECT_CHOICES)
    date = models.DateTimeField(auto_now_add=True, blank=True, null=True)    
    ACTION_CHOICES = (
        ('c', 'create'),
        ('u', 'update'),
        ('d', 'delete'),
    )
    action = models.CharField(max_length=1, choices=ACTION_CHOICES)
    object_pk = models.PositiveIntegerField()   

def save_object(sender, **kwargs):
    o = kwargs['instance']
    if kwargs['created']:
        a = 'create'
    else:
        a = 'update'
    
    log = Log(object_pk=o.pk, object=o._meta.object_name, action=a)
    log.save()

def delete_object(sender, **kwargs):
    o = kwargs['instance']
    log = Log(object_pk=o.pk, object=o._meta.object_name, action='delete')
    log.save()


post_save.connect(save_object, sender=Person)
pre_delete.connect(delete_object, sender=Person)

post_save.connect(save_object, sender=Location)
pre_delete.connect(delete_object, sender=Location)        
