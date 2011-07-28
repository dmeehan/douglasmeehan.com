from django.shortcuts import get_object_or_404
from django.views.generic.list_detail import object_list, object_detail
from level0.portfolio.models import Project, Discipline

def index(request):
    projects = Project.live.all().filter(featured_work=False).order_by("-date")
    featured = Project.work.all().order_by("?")
    disciplines = Discipline.objects.all()
    return object_list(request,
                       queryset=projects,
                       template_object_name='project',
                       template_name='portfolio/portfolio.html',
                       extra_context={'featured': featured,
                                      'disciplines': disciplines,})

def project_list(request):
    projects = Project.live.all().filter(featured_work=False),
    featured = Project.work.all()
    return object_list(request,
                       queryset=projects,
                       template_object_name='project',
                       template_name='portfolio/project_list.html',)

def project_detail(request, slug):
    projects = Project.live.all()
    return object_detail(request,
                         queryset=projects,
                         slug=slug,
                         template_object_name='project',
                         template_name='portfolio/project_detail.html',)
                         
def discipline_list(request):
    disciplines = Discipline.objects.all()
    return object_list(request,
                       queryset=disciplines,
                       template_object_name='discipline',
                       template_name='portfolio/discipline_list.html',)

def discipline_detail(request, slug):
    discipline = get_object_or_404(Discipline, slug=slug)
    return object_list(request,
                       queryset=discipline.project_set.all(),
                       template_object_name='project',
                       template_name='portfolio/portfolio.html',
                       extra_context={ 'discipline': discipline })
                       
                       
def discipline_context_detail(request, slug, context):
    discipline = get_object_or_404(Discipline, slug=slug)
    return object_list(request,
                       queryset=discipline.project_set.filter(context__iexact=context),
                       template_object_name='project',
                       template_name='portfolio/discipline_detail.html',
                       extra_context={ 'discipline': discipline,
                                       'context': context, })

def projects_by_context(request, context):
    projects = Project.live.filter(context__iexact=context)
    return object_list(request,
                       queryset=projects,
                       template_object_name='project',
                       template_name='portfolio/context_detail.html',
                       extra_context={ 'context': context})

def projects_by_category(request, category):
    pass

def projects_by_tag(request, tag):
    pass
