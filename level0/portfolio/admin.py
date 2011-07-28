# portfolio/admin.py

from django.contrib import admin
from django import forms

from level0.portfolio.models import *
from level0.contacts.models import *
#from level0.organize.models import *

class DisciplineInline(admin.TabularInline):
    model = Project.disciplines.through
    extra = 2
    verbose_name = "discipline"
    verbose_name_plural = "disciplines"
    
    # Grappelli options
    allow_add = True
    classes = ('collapse-closed',)
    
class ClientInline(admin.TabularInline):
    model = Client
    extra = 1
    
    # Grappelli options
    allow_add = True
    classes = ('collapse-closed',)
    sort_field_name = "order"
    
class CollaboratorInline(admin.TabularInline):
    model = Collaborator
    extra = 1
    
    # Grappelli options
    allow_add = True
    classes = ('collapse-closed',)
    sort_field_name = "order"

class FirmInline(admin.TabularInline):
    model = Firm
    extra = 1
    
    # Grappelli options
    allow_add = True
    classes = ('collapse-closed',)
    
#class CategoryItemInline(generic.GenericTabularInline):
    #model = CategoryItem
    #extra = 1
    #verbose_name = "category"
    #verbose_name_plural = "categories"
    
    # Grappelli options
    #allow_add = True
    #classes = ('collapse-closed',)
    
class ProjectVisualInline(admin.TabularInline):
    model = ProjectVisual
    verbose_name = "visual"
    verbose_name_plural = "visuals"
    
    # Grappelli options
    allow_add = True
    classes = ('collapse-closed',)
    sort_field_name = "order"
    
class ProjectAudioInline(admin.TabularInline):
    model = ProjectAudio
    verbose_name = "audio"
    verbose_name_plural = "audio"
    
    # Grappelli options
    allow_add = True
    classes = ('collapse-closed',)
    sort_field_name = "order"

class ProjectDocumentInline(admin.TabularInline):
    model = ProjectDocument
    verbose_name = "document"
    verbose_name_plural = "documents"
    
    # Grappelli options
    allow_add = True
    classes = ('collapse-closed',)
    
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'status', 'featured_home', 'featured_work', 'enable_comments', )
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ('status', 'featured_home', 'featured_work', 'enable_comments', )
    
    fieldsets = (
        ('Content', {
            'fields': ('title', 'context', 'date', 'description', 'external_url',)
        }),
        ('Meta', {
            'classes': ('collapse-open',),
            'fields': ('status', 'featured_home', 'featured_work', 'enable_comments', 'tags', 'slug',)
        }),
        ('Studio', {
            'classes': ('collapse-closed',),
            'fields': ('studio',)
        }),
        ('Competition', {
            'classes': ('collapse-closed',),
            'fields': ('competition',)
        }),
    )
    
    inlines = (DisciplineInline, CollaboratorInline, 
               ClientInline, FirmInline, 
               ProjectVisualInline, ProjectAudioInline, ProjectDocumentInline)
    
    # Grappelli options
    order = 0


class CompetitionAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    
    # Grappelli options
    order = 4
    
class ProgramAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    
    # Grappelli options
    order = 3
    
class StudioAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    
    # Grappelli options
    order = 2
    
class DisciplineAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    
    # Grappelli options
    order = 1

class ProjectVisualAdmin(admin.ModelAdmin):
    pass
  
 
admin.site.register(Discipline, DisciplineAdmin)
admin.site.register(Studio, StudioAdmin)
admin.site.register(Competition, CompetitionAdmin)
admin.site.register(Program, ProgramAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectVisual, ProjectVisualAdmin)



