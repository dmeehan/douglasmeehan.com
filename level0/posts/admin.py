# posts/admin.py

from django.contrib import admin
from django.contrib.contenttypes import generic
from django.conf import settings

from level0.posts.models import *


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date', 'status', 'featured', 'enable_comments',)
    prepopulated_fields = {"slug": ("title",)}
    list_editable = ('status', 'featured', 'enable_comments')
    
    fieldsets = (
        (None, {
            'fields': ('posted_by',),
        }),
        ('Content', {
            'fields': ('title', 'excerpt', 'body',),
        }),
        ('Options', {
            'fields' : ('status', 'featured', 'enable_comments', 'pub_date',),
        }),
        ('Metadata', {
            'fields' : ('slug', 'tags',),
        }),
    )
    
    # Media
    class Media:
        js = [
            settings.ADMIN_MEDIA_PREFIX + 'tinymce/jscripts/tiny_mce/tiny_mce.js',
            settings.ADMIN_MEDIA_PREFIX + 'tinymce_setup/tinymce_setup.js',
        ]
        
class LinkAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date',)
    prepopulated_fields = {"slug": ("title",)}
    
    fieldsets = (
        (None, {
            'fields': ('posted_by',),
        }),
        ('Content', {
            'fields': ('title', 'description', 'website', 'via_name', 'via_url', 'tags'),
        }),
        ('Display Options', {
            'fields' : ('status', 'pub_date', 'slug',),
        }),
    )

admin.site.register(Article, ArticleAdmin)
admin.site.register(Link, LinkAdmin)
