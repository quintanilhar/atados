# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models

class Migration(DataMigration):

    def forwards(self, orm):
        from flatblocks.models import FlatBlock
        for slug in {'terms', 'privacy', 'security', 'about'}:
            flatblock = FlatBlock()
            flatblock.content = flatblock.slug = slug
            flatblock.save()

    def backwards(self, orm):
        raise RuntimeError("Cannot reverse this migration.")
        "Write your backwards methods here."

    models = {
        'flatblocks.flatblock': {
            'Meta': {'object_name': 'FlatBlock'},
            'content': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'header': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        }
    }

    complete_apps = ['flatblocks']
    symmetrical = True
