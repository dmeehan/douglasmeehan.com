# organize/admin.py

from django.contrib import admin
from actionmanual.maestro.models import *

class SectionItemInline(admin.TabularInline):
    model = SectionItem
    verbose_name = "section item"
    verbose_name_plural = "section items"
    
    # Grappelli options
    allow_add = True
    
class CategoryItemInline(admin.TabularInline):
    model = CategoryItem
    extra = 1
    verbose_name = "category item"
    verbose_name_plural = "category items"
    
    # Grappelli options
    allow_add = True

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ('name', 'parent', 'description')
    ordering = ['parent']
    inlines = [
        CategoryItemInline
    ]

class SectionAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    inlines = [
        SectionItemInline
    ]
    
admin.site.register(Category, CategoryAdmin)
admin.site.register(Section, SectionAdmin)
