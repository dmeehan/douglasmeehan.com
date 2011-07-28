# /models.py

from django.db import models

from level0.contacts.models import Entity, Person

class Job(models.Model):
    """
    
        A job experience to be listed on the resume
    
    """
    company =
    title = models.CharField(max_length=250)
    start_date = 
    end_date =
    city = 
    state = 
    description =
    
    slug = models.SlugField(unique=True, help_text="Suggested value automatically generated from title. Must be unique.")
    
    def __unicode__(self):
        return u'%s' % (self.name)

class Education(models.Model):
    school =
    degrees = 
    minor =
    activities =
    awards = 
    
    slug = models.SlugField(unique=True, help_text="Suggested value automatically generated from title. Must be unique.")
    
class Skill(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(unique=True, help_text="Suggested value automatically generated from title. Must be unique.")
    
    def __unicode__(self):
        return u'%s' % (self.name)


class Software(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(unique=True, help_text="Suggested value automatically generated from title. Must be unique.")


class Award(models.Model):
    name = models.CharField(max_length=250)
    giver = 
    slug = models.SlugField(unique=True, help_text="Suggested value automatically generated from title. Must be unique.")