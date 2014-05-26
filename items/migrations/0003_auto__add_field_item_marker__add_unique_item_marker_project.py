# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Item.marker'
        db.add_column(u'items_item', 'marker',
                      self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True),
                      keep_default=False)

        # Adding unique constraint on 'Item', fields ['marker', 'project']
        db.create_unique(u'items_item', ['marker', 'project_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'Item', fields ['marker', 'project']
        db.delete_unique(u'items_item', ['marker', 'project_id'])

        # Deleting field 'Item.marker'
        db.delete_column(u'items_item', 'marker')


    models = {
        u'items.item': {
            'Meta': {'ordering': "['id']", 'unique_together': "(('marker', 'project'),)", 'object_name': 'Item'},
            'blocked': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'marker': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            'progress': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['projects.Project']"}),
            'ready': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '500'})
        },
        u'projects.project': {
            'Meta': {'object_name': 'Project'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '500'})
        }
    }

    complete_apps = ['items']