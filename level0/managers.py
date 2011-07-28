# managers.py

from django.db import models

class GetPrevNextManager(models.Manager): 
    def get_next_by_id(self, object): 
        qs = self.filter(id__gt=object.id) 
        if qs.count() > 0: 
            return qs.order_by('id')[0] 
        # empty queryset 
        return qs 
    def get_prev_by_id(self, object): 
        qs = self.filter(id__lt=object.d) 
        if qs.count() > 0: 
            return qs.order_by('-id')[0] 
        # empty queryset 
        return qs 