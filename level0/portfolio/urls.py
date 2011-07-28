# level0/portfolio/urls.py

from django.conf.urls.defaults import *

urlpatterns = patterns('level0.portfolio.views',
    (r'^$', 'index'),
	(r'^projects/(?P<slug>[-\w]+)/$', 'project_detail'),
	(r'^disciplines/$', 'discipline_list'),
    (r'^disciplines/(?P<slug>[-\w]+)/$', 'discipline_detail'),
    (r'^disciplines/(?P<slug>[-\w]+)/(?P<context>[-\w]+)/$', 'discipline_context_detail'),
    (r'^context/(?P<context>[-\w]+)/$', 'projects_by_context'),
    #(r'^categories/$', 'category_list'),
    #(r'^categories/(?P<slug>[-\w]+)/$', 'category_detail'),
    (r'^projects/$', 'project_list'),
    # url(regex, view, kwargs=None, name=None, prefix='')
)