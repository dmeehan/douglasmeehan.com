# cms/views.py

from django.views.generic.list_detail import object_detail
from aio.cms.models import Article
from aio.cms.models import SectionArticleRelation

def article_detail(request, slug, template, extra)
    articles = Article.live.all()
    return object_detail(request, queryset=articles,
                         slug=slug, slug_field=slug_field,
                         template_name = template,
                         extra_context = extra)
                         
                         
