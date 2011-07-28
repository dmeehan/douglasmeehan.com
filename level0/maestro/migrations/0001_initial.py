# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):
    
    def forwards(self, orm):
        
        # Adding model 'Category'
        db.create_table('maestro_category', (
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50, unique=True, db_index=True)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['maestro.Category'], null=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=250)),
        ))
        db.send_create_signal('maestro', ['Category'])

        # Adding unique constraint on 'Category', fields ['parent', 'name']
        db.create_unique('maestro_category', ['parent_id', 'name'])

        # Adding model 'Section'
        db.create_table('maestro_section', (
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50, unique=True, db_index=True)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['maestro.Section'], null=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=250)),
        ))
        db.send_create_signal('maestro', ['Section'])

        # Adding unique constraint on 'Section', fields ['parent', 'name']
        db.create_unique('maestro_section', ['parent_id', 'name'])

        # Adding model 'CategoryItem'
        db.create_table('maestro_categoryitem', (
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(related_name='item_category', to=orm['maestro.Category'])),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType'])),
            ('object_id', self.gf('django.db.models.fields.PositiveIntegerField')()),
        ))
        db.send_create_signal('maestro', ['CategoryItem'])

        # Adding model 'SectionItem'
        db.create_table('maestro_sectionitem', (
            ('name', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('section', self.gf('django.db.models.fields.related.ForeignKey')(related_name='item_section', to=orm['maestro.Section'])),
            ('object_id', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('order', self.gf('django.db.models.fields.IntegerField')(blank=True)),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType'])),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('maestro', ['SectionItem'])
    
    
    def backwards(self, orm):
        
        # Deleting model 'Category'
        db.delete_table('maestro_category')

        # Removing unique constraint on 'Category', fields ['parent', 'name']
        db.delete_unique('maestro_category', ['parent_id', 'name'])

        # Deleting model 'Section'
        db.delete_table('maestro_section')

        # Removing unique constraint on 'Section', fields ['parent', 'name']
        db.delete_unique('maestro_section', ['parent_id', 'name'])

        # Deleting model 'CategoryItem'
        db.delete_table('maestro_categoryitem')

        # Deleting model 'SectionItem'
        db.delete_table('maestro_sectionitem')
    
    
    models = {
        'contenttypes.contenttype': {
            'Meta': {'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'maestro.category': {
            'Meta': {'unique_together': "(('parent', 'name'),)", 'object_name': 'Category'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['maestro.Category']", 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'unique': 'True', 'db_index': 'True'})
        },
        'maestro.categoryitem': {
            'Meta': {'object_name': 'CategoryItem'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'item_category'", 'to': "orm['maestro.Category']"}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {})
        },
        'maestro.section': {
            'Meta': {'unique_together': "(('parent', 'name'),)", 'object_name': 'Section'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['maestro.Section']", 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'unique': 'True', 'db_index': 'True'})
        },
        'maestro.sectionitem': {
            'Meta': {'object_name': 'SectionItem'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'order': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'section': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'item_section'", 'to': "orm['maestro.Section']"})
        }
    }
    
    complete_apps = ['maestro']
