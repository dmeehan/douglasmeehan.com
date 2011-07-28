# maestro/models.py

"""

    A simple CMS app that allow items on a website 
    to be categorized and grouped in sections
    
"""

from django.db import models
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType

from actionmanual.fields import PositionField

class Category(models.Model):
    """
    
    A category that a content object can belong to.
    
    """
    name = models.CharField(max_length=250, help_text="Maximum 250 characters.")
    description = models.TextField(blank=True)
    parent = models.ForeignKey('self', null=True, blank=True, 
                                help_text="Specify parent category if this is a sub-category. Otherwise, leave empty")
    slug = models.SlugField(unique=True, help_text="Suggested value automatically generated from name. Must be unique.")
    
    class Meta:
        unique_together = ('parent', 'name',)
        verbose_name_plural = "Categories"

    def __unicode__(self):
        if self.parent:
            return '%s: %s' % (self.parent, self.name)
        else:
            return self.name

    def get_absolute_url(self):
        pass
        
class Section(models.Model):
    """
    
    A section of a website that a content object can belong to.
    
    """
    name = models.CharField(max_length=250, help_text="Maximum 250 characters.")
    description = models.TextField()
    parent = models.ForeignKey('self', null=True, blank=True, 
                                help_text="Specify parent section if this is a sub-section. Otherwise, leave empty")
    slug = models.SlugField(unique=True, help_text="Suggested value automatically generated from title. Must be unique.")
    
    class Meta:
        unique_together = ('parent', 'name',)
        ordering = ['name']
        
    def save(self, *args, **kwargs):
	   if self.parent:
	       self.name = u'%s: %s' % (self.parent, self.name)
	   super(Section, self).save(*args, **kwargs)
    
    def __unicode__(self):
        return self.name
    
    def get_absolute_url(self):
        pass  
        
class CategoryItem(models.Model):
    """
    
        The relationship between a category and an arbitrary object
        
    """
    category = models.ForeignKey(Category, related_name="item_category")
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey('content_type', 'object_id')
    name = models.CharField(max_length=250, editable=False, null=True) 
    
    
    def __unicode__(self):
        return self.name     
         
    def save(self, *args, **kwargs):
        self.name = self.content_object.__unicode__()
        return super(CategoryItem, self).save(*args, **kwargs)
    
    class Meta:
         ordering = ['content_type']
         verbose_name = "category relation"
        
    
class SectionItem(models.Model):
    """
    
        The relationship between a section and an arbitrary object
        
    """
    order = PositionField(unique_for_field='section')
    section = models.ForeignKey(Section, related_name="item_section")
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey('content_type', 'object_id')
    name = models.CharField(max_length=250, editable=False) 
    
    
    def __unicode__(self):
        return self.name     
         
    def save(self, *args, **kwargs):
        self.name = self.content_object.__unicode__()
        return super(SectionItem, self).save(*args, **kwargs) 
    
    class Meta:
        ordering = ['order', 'content_type', 'object_id']
        verbose_name = "section relation"
