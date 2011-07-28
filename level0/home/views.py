# level0/home/views.py

from django.views.generic.list_detail import object_list, object_detail
from level0.portfolio.models import Project, Discipline

def index(request):
    projects = Project.home.order_by("-date")
    disciplines = Discipline.objects.all()
    return object_list(request,
                       queryset=projects,
                       template_name='home/index.html',)