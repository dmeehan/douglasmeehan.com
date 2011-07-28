# media/admin.py 

from django.contrib import admin

from level0.media.models import *
#from level0.organize.models import CategoryItem

#class CategoryItemInline(generic.GenericTabularInline):
    #model = CategoryItem
    #extra = 1
    #verbose_name = "category"
    #verbose_name_plural = "categories"
    
    # Grappelli options
    #allow_add = True
    #classes = ('collapse-closed',)


class ImageAdmin(admin.ModelAdmin):
    list_display = ('title','admin_thumbnail_view', 'modified_date',)
    ordering = ('-modified_date',)
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title',)
    
    fieldsets = (
        ('Content', {
            'fields': ('title', 'original', 'caption',)
        }),
        ('Meta', {
            'classes': ('collapse-open',),
            'fields': ('public', 'crop_horz', 'crop_vert', 'slug',)
        }),
        ('Categorization', {
            'classes': ('collapse-open',),
            'fields': ('image_type', 'tags',)
        }),
    )
    
    #inlines = (CategoryItemInline,)
    
class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'modified_date',)
    ordering = ('-modified_date',)
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title',)
    
    fieldsets = (
        ('Content', {
            'fields': ('title', 'video', 'poster', 'caption',)
        }),
        ('Meta', {
            'classes': ('collapse-open',),
            'fields': ('public', 'slug',)
        }),
        ('Categorization', {
            'classes': ('collapse-open',),
            'fields': ('tags',)
        }),
    )
    
    #inlines = (CategoryItemInline,)

class FlashAdmin(admin.ModelAdmin):
    list_display = ('title', 'modified_date',)
    ordering = ('-modified_date',)
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title',)
    
    fieldsets = (
        ('Content', {
            'fields': ('title', 'swf', 'poster', 'caption',)
        }),
        ('Meta', {
            'classes': ('collapse-open',),
            'fields': ('public', 'slug',)
        }),
        ('Categorization', {
            'classes': ('collapse-open',),
            'fields': ('tags',)
        }),
    )
    
    #inlines = (CategoryItemInline,)
    
class AudioAdmin(admin.ModelAdmin):
    list_display = ('title', 'modified_date',)
    ordering = ('-modified_date',)
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title',)
    
    fieldsets = (
        ('Content', {
            'fields': ('title', 'audio', 'poster', 'caption',)
        }),
        ('Meta', {
            'classes': ('collapse-open',),
            'fields': ('public', 'slug',)
        }),
        ('Categorization', {
            'classes': ('collapse-open',),
            'fields': ('tags',)
        }),
    )
    
    #inlines = (CategoryItemInline,)
    
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('title', 'modified_date',)
    ordering = ('-modified_date',)
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title',)
    
    fieldsets = (
        ('Content', {
            'fields': ('title', 'document', 'caption',)
        }),
        ('Meta', {
            'classes': ('collapse-open',),
            'fields': ('public', 'slug',)
        }),
        ('Categorization', {
            'classes': ('collapse-open',),
            'fields': ('tags',)
        }),
    )
    
    #inlines = (CategoryItemInline,)
    
class CollectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'caption', 'modified_date',)
    ordering = ('-modified_date',)
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title',)
    filter_horizontal = ('images', 'videos', 'audio', 'documents', )

admin.site.register(Image, ImageAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(Flash, FlashAdmin)
admin.site.register(Audio, AudioAdmin)
admin.site.register(Document, DocumentAdmin)
admin.site.register(Collection, CollectionAdmin)
