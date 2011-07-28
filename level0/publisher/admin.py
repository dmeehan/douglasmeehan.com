# articles/admin.py

from django.contrib import admin
from django import forms
from django.conf import settings
from aio.cms.models import Article, Section, SectionArticleRelation

class SectionArticleRelationForm(forms.ModelForm):
    model = SectionArticleRelation
    class Media:
        js = (
            '/media/js/jquery/jquery-latest.js',
            '/media/js/jquery/ui/jquery-ui.min.js',
            '/media/js/jquery/ui/jquery.ui.sortable.min.js',
            '/media/js/article-sort.js',
        )
    
class SectionArticleInline(admin.TabularInline):
	model = SectionArticleRelation
	extra = 2
	exclude = ('order','featured',)
	verbose_name = "site organization"
	verbose_name_plural = "site organization"
	
	# Grappelli options
	allow_add = True
	sortable = True
	
class ArticleSectionInline(admin.TabularInline):
	model = SectionArticleRelation
	extra = 2
	exclude = ('main','featured',)
	verbose_name = "Articles"
	verbose_name_plural = "Articles"
	
	# Grappelli options
	allow_add = True
	sortable = True
	
class SectionAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ('name', 'parent', 'description',)
    inlines = [
       ArticleSectionInline,
    ]
    
    form = SectionArticleRelationForm

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date','author',)
    prepopulated_fields = {"slug": ("title",)}
    inlines = [
        SectionArticleInline,
    ]
    
    fieldsets = (
        (None, {
            'fields': ('author',),
        }),
        ('Content', {
            'fields': ('title', 'excerpt', 'body', 'image', 'image_size', 'image_location', 'file'),
        }),
        ('Options', {
            'fields' : ('status', 'pub_date', 'slug',),
        }),
    )
    
    form = SectionArticleRelationForm
    
    # Media
    class Media:
        js = [
            settings.ADMIN_MEDIA_PREFIX + 'tinymce/jscripts/tiny_mce/tiny_mce.js',
            settings.ADMIN_MEDIA_PREFIX + 'tinymce_setup/tinymce_setup.js',
        ]
        

admin.site.register(Article, ArticleAdmin)
admin.site.register(Section, SectionAdmin)
