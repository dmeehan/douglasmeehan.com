from django.contrib import admin
from grappelli.sites import GrappelliSite
admin.site = GrappelliSite()
admin.autodiscover()

admin.site.groups = {
    0: {
        'name': 'Add & Edit Custom Content',
        'classes': '',
        'show_apps': False,
        'apps': ['events', 'artists', 'affiliates',]
    },
    1: {
        'name':'Add & Organize Articles',
        'classes': ['collapse-open'],
        'show_apps': False,
        'apps': ['cms',]
    },
    2: {
        'name': 'Manage Users & Profiles',
        'classes': ['collapse-closed'],
        'show_apps': False,
        'apps': ['auth']
    },
    3: {  
        'name': 'Admin Options',
        'classes': ['collapse-closed'],
        'show_apps': False,
        'apps': ['grappelli', 'sites']
    },
}
