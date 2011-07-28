# cms/models.py

import datetime

from django.conf import settings
from django.db import models
from django.db.models import permalink
from django.contrib.auth.models import User
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from django.contrib.comments.models import Comment
from django.contrib.comments.signals import comment_will_be_posted
from django.contrib.comments.moderation import CommentModerator, moderator
from django.contrib.sites.models import Site
from django.utils.encoding import smart_str

from publisher.fields import PositionField

# models for organization of content
class Category(models.Model):
    """
    
    A category that a content object can belong to.
    
    """
    name = models.CharField(max_length=250, help_text="Maximum 250 characters.")
    description = models.TextField()
    parent = models.ForeignKey('self', null=True, blank=True, 
                                help_text="Specify parent category if this is a sub-category. Otherwise, leave empty")
    slug = models.SlugField(unique=True, help_text="Suggested value automatically generated from name. Must be unique.")
    
    class Meta:
        unique_together = ('parent', 'name',)
        ordering = ['name']
        verbose_name_plural = "Categories"
    
    def __unicode__(self):
        if self.parent:
            self.rep = u'%s: %s' % (self.parent.name, self.name)
            return self.rep
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
                                limit_choices_to = {'parent__isnull':True},
                                help_text="Specify parent section if this is a sub-section. Otherwise, leave empty")
    slug = models.SlugField(unique=True, help_text="Suggested value automatically generated from title. Must be unique.")
    
    class Meta:
        unique_together = ('parent', 'name',)
        ordering = ['name']
    
    def save (self, *args, **kwargs):
        if self.parent:
            pieces = self.name.split(':')
            if len(pieces) == 1:
                self.name = u'%s: %s' % (self.parent.name, self.name)
        return super(Section, self).save(*args, **kwargs)
    
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
    object = generic.GenericForeignKey('content_type', 'object_id')
    
    def __unicode__(self):
        name = self.object.__unicode__()
        return name
    
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
    object = generic.GenericForeignKey('content_type', 'object_id')
    name = models.CharField(max_length=250, editable=False) 
    
    
    def __unicode__(self):
        return self.object.__unicode__()        
         
    def save(self, *args, **kwargs):
        self.name = self.object.__unicode__()
        return super(SectionItem, self).save(*args, **kwargs) 
    
    class Meta:
        ordering = ['order', 'content_type', 'object_id']
        verbose_name = "section relation"
		
	
# models for content types
class Article(models.Model):
    """
    
        A story or entry on a website.
    
    """
    #standard Model Manager
    objects = models.Manager()
    
    # custom Model Manager 
    live = LiveManager()

    LIVE_STATUS = 1
    DRAFT_STATUS = 2
    HIDDEN_STATUS = 3
    STATUS_CHOICES = (
        (LIVE_STATUS, 'Live'),
        (DRAFT_STATUS, 'Draft'),
        (HIDDEN_STATUS, 'Hidden'),
    )
    
    IMAGE_SIZE_CHOICES = (
        ('thumbnail', 'Thumb'),
        ('small', 'Small'),
        ('medium', 'Medium'),
        ('large', 'Large'),
    )
    
    IMAGE_LOCATION_CHOICES = (
        ('right', 'Right'),
        ('left', 'Left'),
        ('top', 'Top'),
        ('bottom', 'Bottom'),
    )
    
    # Core fields.
    title = models.CharField(max_length=250, help_text="Maximum 250 characters.")
    excerpt = models.TextField(blank=True, 
                               help_text="""A short summary of the article. Optional.""")
    body = models.TextField()
    pub_date = models.DateTimeField(default=datetime.datetime.now)
    image = FileBrowseField("Image", format='Image', max_length=200, blank=True, null=True,
                            help_text="Valid file formats: .jpg, .png")
    image_size = models.CharField(choices=IMAGE_SIZE_CHOICES, max_length=50, 
	                            default='small')
    image_location = models.CharField(choices=IMAGE_LOCATION_CHOICES, max_length=50, 
	                            default='right')
    file = FileBrowseField("Document", format='Document', max_length=200, blank=True, null=True,
                           help_text="Valid file formats: .pdf, .doc, .xls, .txt, .rtf")
    
    # Metadata.
    author = models.ForeignKey(User)
    enable_comments = models.BooleanField(default=False)
    slug = models.SlugField(unique_for_date='pub_date', 
	                        help_text="""Suggested value automatically 
							             generated from title. Must be unique.""")
    status = models.IntegerField(choices=STATUS_CHOICES, 
	                             default=LIVE_STATUS, 
								 help_text="""Only entries with live status 
								            will be publicly displayed.""")
    
    class Meta:
        ordering = ['-pub_date']
        
    def __unicode__(self):
        return self.title
        
    def get_absolute_url(self):
       pass
	   
class ArticleModerator(CommentModerator):
	enable_field = 'enable_comments'
	auto_moderate_field = 'pub_date'
	auto_close_field = 'pub_date'
	moderate_after = settings.COMMENTS_MODERATE_AFTER
	close_after = settings.COMMENTS_CLOSE_AFTER
	email_notification = True
	
	def check_spam(self, request, comment, key, blog_url=None, base_url=None):
		try:
			from akismet import Akismet
		except:
			return False

		if blog_url is None:
			blog_url = 'http://%s/' % Site.objects.get_current().domain

		ak = Akismet(
			key=settings.AKISMET_API_KEY,
			blog_url=blog_url
		)

		if base_url is not None:
			ak.baseurl = base_url

		if ak.verify_key():
			data = {
				'user_ip': request.META.get('REMOTE_ADDR', '127.0.0.1'),
				'user_agent': request.META.get('HTTP_USER_AGENT', ''),
				'referrer': request.META.get('HTTP_REFERER', ''),
				'comment_type': 'comment',
				'comment_author': comment.user_name.encode('utf-8'),
			}

			if ak.comment_check(comment.comment.encode('utf-8'), data=data, build_data=True):
				return True

		return False

	def allow(self, comment, content_object, request):
		allow = super(ArticleModerator, self).allow(comment, content_object, request)

		# change this depending on which spam provider you want to use
		spam = self.check_spam(request, comment,
			key=settings.AKISMET_API_KEY,
		)

		return not spam and allow

moderator.register(Article, ArticleModerator)
    
class SectionArticleRelation(models.Model):
	"""
    
        The relationship between an article and its section within the site
        
	"""
	
	FULL_DISPLAY = 1
	EXCERPT_DISPLAY = 2
	LINK_DISPLAY = 3
	DISPLAY_OPTIONS = (
		(FULL_DISPLAY, 'Full'),
		(EXCERPT_DISPLAY, 'Excerpt'),
		(LINK_DISPLAY, 'Link'),
	)
	order = PositionField(unique_for_field='section')
	featured = models.BooleanField()
	article = models.ForeignKey(Article)
	section = models.ForeignKey(Section, related_name='article_section')
	main = models.BooleanField(verbose_name="main section?")
	display = models.IntegerField(choices=DISPLAY_OPTIONS, 
	                             default=FULL_DISPLAY,
								 verbose_name="article display")
	
	main_section=models.CharField(max_length=250, editable=False)
	
	class Meta:
	   ordering = ['order', 'main', 'article', 'section', 'display'] 
		
	def save (self, *args, **kwargs):
		related_articles = self._default_manager.filter(article=self.article)
		if self.main:
			related_articles.update(main=False)
			related_articles.update(main_section=self.section.name)
			self.main_section = self.section.name
		else:
			if not related_articles:
				self.main_section = self.section.name
				self.main = True
			else:
				self.main_section = related_articles[0].main_section
		return super(SectionArticleRelation, self).save(*args, **kwargs)
		
	@permalink
	def get_absolute_url(self):
           slug = self.article.slug
           section = self.main_section
	   view = section + '_article_detail'
	   return (view, slug)

class Link(models.Model):
	"""
    
        A link to an external source
    
    """
	pass
