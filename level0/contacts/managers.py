# contacts/managers.py

from django.db import models
from django.db.models.query import QuerySet


class SubclassingQuerySet(QuerySet):
    """
       
       A method of fetching a model's subclassed version from an instance.
       From http://www.djangosnippets.org/snippets/1034/
       
    """
    
    def __getitem__(self, k):
        result = super(SubclassingQuerySet, self).__getitem__(k)
        if isinstance(result, models.Model) :
            return result.as_leaf_class()
        else :
            return result
    def __iter__(self):
        for item in super(SubclassingQuerySet, self).__iter__():
            yield item.as_leaf_class()
            
class ContactManager(models.Manager):
    def get_query_set(self):
        return SubclassingQuerySet(self.model)