from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    #(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    
    # redirects
    (r'^portfolio/', 'django.views.generic.simple.redirect_to', {'url': '/work/'}),
    (r'^portfolio/slideshow.php', 'django.views.generic.simple.redirect_to', {'url': '/work/'}),
    (r'^pdf/douglas_meehan.pdf', 'django.views.generic.simple.redirect_to', {'url': '/media/docs/douglas_meehan_resume.pdf'}),
    (r'^pdf/douglas_meehan_portfolio.pdf', 'django.views.generic.simple.redirect_to', {'url': '/media/docs/douglas_meehan_portfolio.pdf'}),

    # django-filebrower admin extension:
    #(r'^admin/filebrowser/', include('filebrowser.urls')),
    
    # django-grappelli admin extension:
    #(r'^grappelli/', include('grappelli.urls')),

    # Administration interface:
    (r'^admin/', include(admin.site.urls)),
    
    
    # django-tinymce admin extension
    #(r'^tinymce/', include('tinymce.urls')),
    
    #(r'^$', include('level.portfolio.urls')),
    
    # Homepage:
    (r'^$', 'django.views.generic.simple.redirect_to', {'url': '/about/', 'permanent': False}),
    
    # Portfolio:
    #(r'^work/', include('level0.portfolio.urls')),
    
    # About:
    (r'^about/', 'level0.about.views.about_index'),

    # Blog
    #(r'^words/', include('basic.blog.urls')),
    
    # Sections:
    #(r'^(?P<section>\w+)/$', 'level0.organize.views.section_index'),
    
    # Comments:
    #(r'^comments/', include('django.contrib.comments.urls')),

    # Flatpages. This should always go last as a catch-all:
    #(r'', include('django.contrib.flatpages.urls')),
)
