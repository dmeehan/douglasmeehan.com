# portfolio/managers.py

from django.db import models

class LiveProjectManager(models.Manager):
    def get_query_set(self):
        return super(LiveProjectManager, self).get_query_set().filter(status=self.model.LIVE_STATUS)


class FeaturedHomeManager(models.Manager):
    def get_query_set(self):
        return super(FeaturedHomeManager, self).get_query_set().filter(status=self.model.LIVE_STATUS).filter(featured_home=True)
        

class FeaturedWorkManager(models.Manager):
    def get_query_set(self):
        return super(FeaturedWorkManager, self).get_query_set().filter(status=self.model.LIVE_STATUS).filter(featured_work=True)