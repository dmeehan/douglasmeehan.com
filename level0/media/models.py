# media/models.py

"""

    Models for the Media app, which organizes, processes, stores,
    and retrieves files on a website.

    Douglas Meehan
    dmeehan@gmail.com
    
""" 

from django.db import models
from django.db.models import permalink
from django.contrib.auth.models import User   
from django.conf import settings        
from django.contrib.contenttypes import generic  


from tagging.fields import TagField
    
class File(models.Model):
    """
     
        An abstract model that defines fields, information, and methods 
        common across all file types
     
     
    """

    # Core file fields.
    title = models.CharField(max_length=255)
    caption = models.TextField(blank=True)
    public = models.BooleanField(help_text="This file is publicly available", default=True)
    
    # Metadata.
    slug = models.SlugField(unique=True)
    creation_date = models.DateTimeField(auto_now_add=True, editable=False)
    modified_date = models.DateTimeField(auto_now=True, editable=False)
    
    # Categorization
    tags = TagField(blank=True, null=True)
        
    class Meta:
        ordering = ('-creation_date',)
        abstract = True
        
    def __unicode__(self):
        return '%s' % self.title
 

class Image(File):
    """
    
        An image file, such as a photograph or other rasterized image.
    
    """
    
    DRAWING = 1
    PHOTOGRAPH = 2
    RENDERING = 3
    SCREENSHOT = 4
    MODEL = 5
    IMAGE_CHOICES = (
        (DRAWING, 'Drawing'),
        (PHOTOGRAPH, 'Photograph'),
        (RENDERING, 'Rendering'),
        (SCREENSHOT, 'Screenshot'),
        (MODEL, 'model'),
    )
    
    LEFT = 0
    CENTER = 1
    RIGHT = 2
    CROPHORZ_CHOICES = (
        (LEFT, 'LEFT'),
        (CENTER, 'CENTER'),
        (RIGHT, 'RIGHT'),
    )
    
    TOP = 0
    CENTER = 1
    BOTTOM = 2
    CROPVERT_CHOICES = (
        (TOP, 'TOP'),
        (CENTER, 'CENTER'),
        (BOTTOM, 'BOTTOM'),
    )
    
    # Core image fields.
    original = models.ImageField(upload_to='images')
    crop_horz = models.PositiveSmallIntegerField(verbose_name='horizontal cropping', 
                                    choices=CROPHORZ_CHOICES, 
                                    blank=True,
                                    default=CENTER,
                                    help_text="From where to horizontally crop the image, if cropping is necessary.")
                                     
    crop_vert = models.PositiveSmallIntegerField(verbose_name='vertical cropping', 
                                    choices=CROPVERT_CHOICES, 
                                    blank=True,
                                    default=CENTER,
                                    help_text="From were to vertically crop the image, if cropping is necessary.")

    image_type = models.PositiveSmallIntegerField(verbose_name="type", choices=IMAGE_CHOICES, default=DRAWING)


class Video(File):
    """
    
        A file with moving images such as .mov, etc
        
    """
    
    # Core Video fields.
    video = models.FileField(upload_to='videos')
    poster = models.ForeignKey(Image, blank=True, null=True)
        
class Flash(File):
    """
    
        A Flash animation
        
    """
    
    # Core Video fields.
    swf = models.FileField(upload_to='swfs')
    poster = models.ForeignKey(Image, blank=True, null=True)

    class Meta:
        verbose_name = "swf"
        verbose_name_plural = "swfs"
        
        
class Audio(File):
    """
    
        A file with sound data such as an .mp3
        
    """
    
    # Core Audio fields.
    audio = models.FileField(upload_to='audio')
    poster = models.ForeignKey(Image, blank=True, null=True)
    
    class Meta:
        verbose_name_plural = "Audio"
        db_table = 'media_audio'
        
class Document(File):
    """
    
    Other file types.
    
    """
    
    # Core Document fields.
    document = models.FileField(upload_to='docs')
    
class Collection(models.Model):
    """
    
    Defines a group of files.
     
    """
    
    # Core fields.
    title = models.CharField(max_length=255, unique=True)
    caption = models.TextField(blank=True)
    public = models.BooleanField(help_text="This collection is publicly available.", default=True)
    
    # Files.
    images = models.ManyToManyField(Image, blank=True, null=True)
    swfs = models.ManyToManyField(Flash, blank=True, null=True)
    documents = models.ManyToManyField(Document, blank=True, null=True)
    videos = models.ManyToManyField(Video, blank=True, null=True)
    audio = models.ManyToManyField(Audio, blank=True, null=True)
    
    # Metadata.
    slug = models.SlugField(unique=True)
    creation_date = models.DateTimeField(auto_now_add=True, editable=False)
    modified_date = models.DateTimeField(auto_now=True, editable=False)
    
    # Categorization
    tags = TagField(null=True,blank=True)
    
       
    class Meta:
        ordering = ['-creation_date']
        get_latest_by = 'creation_date'

    def __unicode__(self):
        return '%s' % self.title
        
