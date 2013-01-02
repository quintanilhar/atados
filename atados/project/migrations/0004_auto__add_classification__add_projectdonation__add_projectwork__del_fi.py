# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Classification'
        db.create_table('project_classification', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal('project', ['Classification'])

        # Adding model 'ProjectDonation'
        db.create_table('project_projectdonation', (
            ('project_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['project.Project'], unique=True, primary_key=True)),
            ('collection_by_organisation', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('delivery_by_donor', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('project', ['ProjectDonation'])

        # Adding model 'ProjectWork'
        db.create_table('project_projectwork', (
            ('project_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['project.Project'], unique=True, primary_key=True)),
            ('classification', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['project.Classification'])),
            ('monthly_hours', self.gf('django.db.models.fields.IntegerField')()),
            ('can_be_done_remotely', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('project', ['ProjectWork'])

        # Deleting field 'Project.where'
        db.delete_column('project_project', 'where')

        # Deleting field 'Project.when'
        db.delete_column('project_project', 'when')

        # Deleting field 'Project.how_long'
        db.delete_column('project_project', 'how_long')

        # Adding field 'Project.responsible'
        db.add_column('project_project', 'responsible',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=50),
                      keep_default=False)

        # Adding field 'Project.phone'
        db.add_column('project_project', 'phone',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=20),
                      keep_default=False)

        # Adding field 'Project.email'
        db.add_column('project_project', 'email',
                      self.gf('django.db.models.fields.EmailField')(default='', max_length=75, blank=True),
                      keep_default=False)

        # Adding field 'Project.addressline'
        db.add_column('project_project', 'addressline',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=200),
                      keep_default=False)

        # Adding field 'Project.neighborhood'
        db.add_column('project_project', 'neighborhood',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=50),
                      keep_default=False)

        # Adding field 'Project.city'
        db.add_column('project_project', 'city',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=50),
                      keep_default=False)


        # Changing field 'Project.details'
        db.alter_column('project_project', 'details', self.gf('django.db.models.fields.TextField')(max_length=1024))

    def backwards(self, orm):
        # Deleting model 'Classification'
        db.delete_table('project_classification')

        # Deleting model 'ProjectDonation'
        db.delete_table('project_projectdonation')

        # Deleting model 'ProjectWork'
        db.delete_table('project_projectwork')

        # Adding field 'Project.where'
        db.add_column('project_project', 'where',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100),
                      keep_default=False)

        # Adding field 'Project.when'
        db.add_column('project_project', 'when',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=30),
                      keep_default=False)

        # Adding field 'Project.how_long'
        db.add_column('project_project', 'how_long',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=30),
                      keep_default=False)

        # Deleting field 'Project.responsible'
        db.delete_column('project_project', 'responsible')

        # Deleting field 'Project.phone'
        db.delete_column('project_project', 'phone')

        # Deleting field 'Project.email'
        db.delete_column('project_project', 'email')

        # Deleting field 'Project.addressline'
        db.delete_column('project_project', 'addressline')

        # Deleting field 'Project.neighborhood'
        db.delete_column('project_project', 'neighborhood')

        # Deleting field 'Project.city'
        db.delete_column('project_project', 'city')


        # Changing field 'Project.details'
        db.alter_column('project_project', 'details', self.gf('django.db.models.fields.TextField')(max_length=500))

    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'organisation.organisation': {
            'Meta': {'object_name': 'Organisation'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'project.classification': {
            'Meta': {'object_name': 'Classification'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'project.project': {
            'Meta': {'unique_together': "(('slug', 'organisation'),)", 'object_name': 'Project'},
            'addressline': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'details': ('django.db.models.fields.TextField', [], {'max_length': '1024'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'neighborhood': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'organisation': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['organisation.Organisation']"}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'responsible': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'})
        },
        'project.projectdonation': {
            'Meta': {'object_name': 'ProjectDonation', '_ormbases': ['project.Project']},
            'collection_by_organisation': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'delivery_by_donor': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'project_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['project.Project']", 'unique': 'True', 'primary_key': 'True'})
        },
        'project.projectwork': {
            'Meta': {'object_name': 'ProjectWork', '_ormbases': ['project.Project']},
            'can_be_done_remotely': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'classification': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['project.Classification']"}),
            'monthly_hours': ('django.db.models.fields.IntegerField', [], {}),
            'project_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['project.Project']", 'unique': 'True', 'primary_key': 'True'})
        }
    }

    complete_apps = ['project']