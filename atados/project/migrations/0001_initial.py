# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Availability'
        db.create_table('project_availability', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('weekday', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('period', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
        ))
        db.send_create_signal('project', ['Availability'])

        # Adding model 'Cause'
        db.create_table('project_cause', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal('project', ['Cause'])

        # Adding model 'Skill'
        db.create_table('project_skill', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal('project', ['Skill'])

        # Adding model 'Apply'
        db.create_table('project_apply', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('volunteer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['volunteer.Volunteer'])),
        ))
        db.send_create_signal('project', ['Apply'])

        # Adding model 'ProjectDonation'
        db.create_table('project_projectdonation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nonprofit', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['nonprofit.Nonprofit'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('details', self.gf('django.db.models.fields.TextField')(max_length=1024)),
            ('responsible', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('zipcode', self.gf('django.db.models.fields.CharField')(default=None, max_length=10, null=True, blank=True)),
            ('addressline', self.gf('django.db.models.fields.CharField')(default=None, max_length=200, null=True, blank=True)),
            ('neighborhood', self.gf('django.db.models.fields.CharField')(default=None, max_length=50, null=True, blank=True)),
            ('city', self.gf('django.db.models.fields.CharField')(default=None, max_length=50, null=True, blank=True)),
            ('vacancies', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=None, null=True, blank=True)),
            ('published', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('deleted', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('deleted_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('image', self.gf('sorl.thumbnail.fields.ImageField')(default=None, max_length=100, null=True, blank=True)),
            ('collection_by_nonprofit', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('project', ['ProjectDonation'])

        # Adding unique constraint on 'ProjectDonation', fields ['slug', 'nonprofit']
        db.create_unique('project_projectdonation', ['slug', 'nonprofit_id'])

        # Adding M2M table for field causes on 'ProjectDonation'
        db.create_table('project_projectdonation_causes', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('projectdonation', models.ForeignKey(orm['project.projectdonation'], null=False)),
            ('cause', models.ForeignKey(orm['project.cause'], null=False))
        ))
        db.create_unique('project_projectdonation_causes', ['projectdonation_id', 'cause_id'])

        # Adding M2M table for field applies on 'ProjectDonation'
        db.create_table('project_projectdonation_applies', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('projectdonation', models.ForeignKey(orm['project.projectdonation'], null=False)),
            ('apply', models.ForeignKey(orm['project.apply'], null=False))
        ))
        db.create_unique('project_projectdonation_applies', ['projectdonation_id', 'apply_id'])

        # Adding model 'ProjectWork'
        db.create_table('project_projectwork', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nonprofit', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['nonprofit.Nonprofit'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('details', self.gf('django.db.models.fields.TextField')(max_length=1024)),
            ('responsible', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('zipcode', self.gf('django.db.models.fields.CharField')(default=None, max_length=10, null=True, blank=True)),
            ('addressline', self.gf('django.db.models.fields.CharField')(default=None, max_length=200, null=True, blank=True)),
            ('neighborhood', self.gf('django.db.models.fields.CharField')(default=None, max_length=50, null=True, blank=True)),
            ('city', self.gf('django.db.models.fields.CharField')(default=None, max_length=50, null=True, blank=True)),
            ('vacancies', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=None, null=True, blank=True)),
            ('published', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('deleted', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('deleted_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('image', self.gf('sorl.thumbnail.fields.ImageField')(default=None, max_length=100, null=True, blank=True)),
            ('prerequisites', self.gf('django.db.models.fields.TextField')(max_length=1024)),
            ('weekly_hours', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True, blank=True)),
            ('can_be_done_remotely', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('project', ['ProjectWork'])

        # Adding unique constraint on 'ProjectWork', fields ['slug', 'nonprofit']
        db.create_unique('project_projectwork', ['slug', 'nonprofit_id'])

        # Adding M2M table for field causes on 'ProjectWork'
        db.create_table('project_projectwork_causes', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('projectwork', models.ForeignKey(orm['project.projectwork'], null=False)),
            ('cause', models.ForeignKey(orm['project.cause'], null=False))
        ))
        db.create_unique('project_projectwork_causes', ['projectwork_id', 'cause_id'])

        # Adding M2M table for field applies on 'ProjectWork'
        db.create_table('project_projectwork_applies', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('projectwork', models.ForeignKey(orm['project.projectwork'], null=False)),
            ('apply', models.ForeignKey(orm['project.apply'], null=False))
        ))
        db.create_unique('project_projectwork_applies', ['projectwork_id', 'apply_id'])

        # Adding M2M table for field availabilities on 'ProjectWork'
        db.create_table('project_projectwork_availabilities', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('projectwork', models.ForeignKey(orm['project.projectwork'], null=False)),
            ('availability', models.ForeignKey(orm['project.availability'], null=False))
        ))
        db.create_unique('project_projectwork_availabilities', ['projectwork_id', 'availability_id'])

        # Adding M2M table for field skills on 'ProjectWork'
        db.create_table('project_projectwork_skills', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('projectwork', models.ForeignKey(orm['project.projectwork'], null=False)),
            ('skill', models.ForeignKey(orm['project.skill'], null=False))
        ))
        db.create_unique('project_projectwork_skills', ['projectwork_id', 'skill_id'])

        # Adding model 'ProjectJob'
        db.create_table('project_projectjob', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nonprofit', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['nonprofit.Nonprofit'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('details', self.gf('django.db.models.fields.TextField')(max_length=1024)),
            ('responsible', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('zipcode', self.gf('django.db.models.fields.CharField')(default=None, max_length=10, null=True, blank=True)),
            ('addressline', self.gf('django.db.models.fields.CharField')(default=None, max_length=200, null=True, blank=True)),
            ('neighborhood', self.gf('django.db.models.fields.CharField')(default=None, max_length=50, null=True, blank=True)),
            ('city', self.gf('django.db.models.fields.CharField')(default=None, max_length=50, null=True, blank=True)),
            ('vacancies', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=None, null=True, blank=True)),
            ('published', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('deleted', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('deleted_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('image', self.gf('sorl.thumbnail.fields.ImageField')(default=None, max_length=100, null=True, blank=True)),
            ('prerequisites', self.gf('django.db.models.fields.TextField')(max_length=1024)),
            ('weekly_hours', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True, blank=True)),
            ('can_be_done_remotely', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('project', ['ProjectJob'])

        # Adding unique constraint on 'ProjectJob', fields ['slug', 'nonprofit']
        db.create_unique('project_projectjob', ['slug', 'nonprofit_id'])

        # Adding M2M table for field causes on 'ProjectJob'
        db.create_table('project_projectjob_causes', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('projectjob', models.ForeignKey(orm['project.projectjob'], null=False)),
            ('cause', models.ForeignKey(orm['project.cause'], null=False))
        ))
        db.create_unique('project_projectjob_causes', ['projectjob_id', 'cause_id'])

        # Adding M2M table for field applies on 'ProjectJob'
        db.create_table('project_projectjob_applies', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('projectjob', models.ForeignKey(orm['project.projectjob'], null=False)),
            ('apply', models.ForeignKey(orm['project.apply'], null=False))
        ))
        db.create_unique('project_projectjob_applies', ['projectjob_id', 'apply_id'])

        # Adding M2M table for field availabilities on 'ProjectJob'
        db.create_table('project_projectjob_availabilities', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('projectjob', models.ForeignKey(orm['project.projectjob'], null=False)),
            ('availability', models.ForeignKey(orm['project.availability'], null=False))
        ))
        db.create_unique('project_projectjob_availabilities', ['projectjob_id', 'availability_id'])

        # Adding M2M table for field skills on 'ProjectJob'
        db.create_table('project_projectjob_skills', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('projectjob', models.ForeignKey(orm['project.projectjob'], null=False)),
            ('skill', models.ForeignKey(orm['project.skill'], null=False))
        ))
        db.create_unique('project_projectjob_skills', ['projectjob_id', 'skill_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'ProjectJob', fields ['slug', 'nonprofit']
        db.delete_unique('project_projectjob', ['slug', 'nonprofit_id'])

        # Removing unique constraint on 'ProjectWork', fields ['slug', 'nonprofit']
        db.delete_unique('project_projectwork', ['slug', 'nonprofit_id'])

        # Removing unique constraint on 'ProjectDonation', fields ['slug', 'nonprofit']
        db.delete_unique('project_projectdonation', ['slug', 'nonprofit_id'])

        # Deleting model 'Availability'
        db.delete_table('project_availability')

        # Deleting model 'Cause'
        db.delete_table('project_cause')

        # Deleting model 'Skill'
        db.delete_table('project_skill')

        # Deleting model 'Apply'
        db.delete_table('project_apply')

        # Deleting model 'ProjectDonation'
        db.delete_table('project_projectdonation')

        # Removing M2M table for field causes on 'ProjectDonation'
        db.delete_table('project_projectdonation_causes')

        # Removing M2M table for field applies on 'ProjectDonation'
        db.delete_table('project_projectdonation_applies')

        # Deleting model 'ProjectWork'
        db.delete_table('project_projectwork')

        # Removing M2M table for field causes on 'ProjectWork'
        db.delete_table('project_projectwork_causes')

        # Removing M2M table for field applies on 'ProjectWork'
        db.delete_table('project_projectwork_applies')

        # Removing M2M table for field availabilities on 'ProjectWork'
        db.delete_table('project_projectwork_availabilities')

        # Removing M2M table for field skills on 'ProjectWork'
        db.delete_table('project_projectwork_skills')

        # Deleting model 'ProjectJob'
        db.delete_table('project_projectjob')

        # Removing M2M table for field causes on 'ProjectJob'
        db.delete_table('project_projectjob_causes')

        # Removing M2M table for field applies on 'ProjectJob'
        db.delete_table('project_projectjob_applies')

        # Removing M2M table for field availabilities on 'ProjectJob'
        db.delete_table('project_projectjob_availabilities')

        # Removing M2M table for field skills on 'ProjectJob'
        db.delete_table('project_projectjob_skills')


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
        'nonprofit.nonprofit': {
            'Meta': {'object_name': 'Nonprofit'},
            'addressline': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'details': ('django.db.models.fields.TextField', [], {'default': 'None', 'max_length': '1024', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('sorl.thumbnail.fields.ImageField', [], {'default': 'None', 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'neighborhood': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'zipcode': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '10', 'null': 'True', 'blank': 'True'})
        },
        'project.apply': {
            'Meta': {'object_name': 'Apply'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'volunteer': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['volunteer.Volunteer']"})
        },
        'project.availability': {
            'Meta': {'object_name': 'Availability'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'period': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'weekday': ('django.db.models.fields.PositiveSmallIntegerField', [], {})
        },
        'project.cause': {
            'Meta': {'object_name': 'Cause'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'project.projectdonation': {
            'Meta': {'unique_together': "(('slug', 'nonprofit'),)", 'object_name': 'ProjectDonation'},
            'addressline': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'applies': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'projectdonation_related'", 'symmetrical': 'False', 'to': "orm['project.Apply']"}),
            'causes': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['project.Cause']", 'symmetrical': 'False'}),
            'city': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'collection_by_nonprofit': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'deleted_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'details': ('django.db.models.fields.TextField', [], {'max_length': '1024'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('sorl.thumbnail.fields.ImageField', [], {'default': 'None', 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'neighborhood': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'nonprofit': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['nonprofit.Nonprofit']"}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'responsible': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'vacancies': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'zipcode': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '10', 'null': 'True', 'blank': 'True'})
        },
        'project.projectjob': {
            'Meta': {'unique_together': "(('slug', 'nonprofit'),)", 'object_name': 'ProjectJob'},
            'addressline': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'applies': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'projectjob_related'", 'symmetrical': 'False', 'to': "orm['project.Apply']"}),
            'availabilities': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['project.Availability']", 'symmetrical': 'False'}),
            'can_be_done_remotely': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'causes': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['project.Cause']", 'symmetrical': 'False'}),
            'city': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'deleted_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'details': ('django.db.models.fields.TextField', [], {'max_length': '1024'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('sorl.thumbnail.fields.ImageField', [], {'default': 'None', 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'neighborhood': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'nonprofit': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['nonprofit.Nonprofit']"}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'prerequisites': ('django.db.models.fields.TextField', [], {'max_length': '1024'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'responsible': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'skills': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['project.Skill']", 'symmetrical': 'False'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'vacancies': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'weekly_hours': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'zipcode': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '10', 'null': 'True', 'blank': 'True'})
        },
        'project.projectwork': {
            'Meta': {'unique_together': "(('slug', 'nonprofit'),)", 'object_name': 'ProjectWork'},
            'addressline': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'applies': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'projectwork_related'", 'symmetrical': 'False', 'to': "orm['project.Apply']"}),
            'availabilities': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['project.Availability']", 'symmetrical': 'False'}),
            'can_be_done_remotely': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'causes': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['project.Cause']", 'symmetrical': 'False'}),
            'city': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'deleted_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'details': ('django.db.models.fields.TextField', [], {'max_length': '1024'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('sorl.thumbnail.fields.ImageField', [], {'default': 'None', 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'neighborhood': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'nonprofit': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['nonprofit.Nonprofit']"}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'prerequisites': ('django.db.models.fields.TextField', [], {'max_length': '1024'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'responsible': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'skills': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['project.Skill']", 'symmetrical': 'False'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'vacancies': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'weekly_hours': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'zipcode': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '10', 'null': 'True', 'blank': 'True'})
        },
        'project.skill': {
            'Meta': {'object_name': 'Skill'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'volunteer.volunteer': {
            'Meta': {'object_name': 'Volunteer'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('sorl.thumbnail.fields.ImageField', [], {'default': 'None', 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        }
    }

    complete_apps = ['project']