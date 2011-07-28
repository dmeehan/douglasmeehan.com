# about/views.py

from django.views.generic.list_detail import object_list, object_detail
from level0.portfolio.models import Project

def about_index(request):
    projects = Project.live.all().order_by('?')[:14]
    return object_list(request,
                       queryset=projects,
                       template_object_name='project',
                       template_name='about/about_index.html',)