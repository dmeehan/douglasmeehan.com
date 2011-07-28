# contacts/models.py

from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic

from level0.contacts.fields import CountryField

class Contact(models.Model):
    """
    
    Generic abstract contact model. Includes fields shared
    between all contact types.
        
    """
    address_line1 = models.CharField(max_length=250, blank=True)
    address_line2 = models.CharField(max_length=250, blank=True)
    city = models.CharField(max_length=100, blank=True)
    state = models.CharField('state/province', max_length=100, blank=True)
    code = models.CharField(max_length=20, blank=True)
    country = CountryField(blank=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=50, blank=True)
    fax = models.CharField(max_length=50, blank=True)
    website = models.URLField(blank=True, verify_exists=True)
    slug = models.SlugField(unique=True)
    
    class Meta:
        abstract = True
    
    def __unicode__(self):
        return u'%s' % self.slug

        
class Entity(Contact):
    """
    
    A contact that is a company, school, government body, etc.
    Inherits from Contact.
    
    """
    
    COMPANY = 1
    SCHOOL = 2
    NONPROFIT = 3
    GOVERNMENT = 4
    ENTITY_CHOICES = (
        (COMPANY, 'Company'),
        (SCHOOL, 'School'),
        (NONPROFIT, 'Non-Profit'),
        (GOVERNMENT, 'Government body'),
    )

    name = models.CharField(max_length=100)
    kind = models.PositiveSmallIntegerField("type", choices=ENTITY_CHOICES)

        
    class Meta:
        verbose_name_plural = "entities"
        db_table = "contacts_entities"
        
    def __unicode__(self):
        return u'%s' % self.name
        
        
class Person(Contact):
    """
    
    A contact that is a person. Inherits from Contact.
    
    """
    GENDER_CHOICES = (
        (1, 'Male'),
        (2, 'Female'),
    )
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100)
    gender = models.PositiveSmallIntegerField(choices=GENDER_CHOICES, blank=True)
    birth_date = models.DateField(blank=True, null=True)
    mobile = models.CharField(max_length=50, blank=True)
    employers = models.ManyToManyField(Entity, blank=True, null=True)


    class Meta:
        verbose_name = "person"
        verbose_name_plural = "people"
        db_table = "contacts_people"

    @property
    def full_name(self):
        return u'%s %s' % (self.first_name, self.last_name)
        
    def __unicode__(self):
        return u'%s' % self.full_name