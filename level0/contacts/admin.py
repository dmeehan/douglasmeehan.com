# contacts/admin.py

from django.contrib import admin
from level0.contacts.models import Person, Entity

class PersonAdmin(admin.ModelAdmin):
	list_display = ('last_name', 'first_name',)
	ordering = ('last_name', 'first_name',)
	search_fields = ('first_name', 'last_name',)
	prepopulated_fields = {'slug': ('first_name','last_name',)}
	fields = ('first_name', 'middle_name', 'last_name', 'address_line1', 'address_line2', 
	          'city', 'state', 'code', 'country', 
	          'email', 'phone', 'fax', 'mobile', 'website', 'gender', 'birth_date', 
	          'employers', 'slug', )
	
class EntityAdmin(admin.ModelAdmin):
	list_display = ('name',)
	ordering = ('name',)
	search_fields = ('name',)
	prepopulated_fields = {'slug': ('name',)}
	fields = ('name', 'kind', 'address_line1', 'address_line2', 
	          'city', 'state', 'code', 'country',
	          'email', 'phone', 'fax', 
	          'website', 'slug', )


admin.site.register(Person, PersonAdmin)
admin.site.register(Entity, EntityAdmin)