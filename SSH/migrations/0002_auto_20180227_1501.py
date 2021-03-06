# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-02-27 14:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SSH', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(blank=True, max_length=200, null=True)),
                ('app_time', models.TimeField()),
                ('app_date', models.DateField()),
                ('app_message', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='image_doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image1', models.FileField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.RenameField(
            model_name='patient',
            old_name='city',
            new_name='gender',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='country',
        ),
        migrations.AddField(
            model_name='doctor',
            name='gender',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='state',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='image_doctor',
            name='doc_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='SSH.doctor'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='doc_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='SSH.doctor'),
        ),
    ]
