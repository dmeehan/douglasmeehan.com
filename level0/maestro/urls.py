# maestro/urls.py

from django.conf.urls.defaults import *

from floatkit.maestro.models import *

urlpatterns = patterns('',
    (r'^(?P<section>[-w]+)/$', 'floatkit.maestro.views.section_index'),
)