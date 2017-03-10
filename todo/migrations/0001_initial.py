# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-08 23:36
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('what_todo', models.CharField(max_length=300)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('execution_date', models.DateField()),
                ('mini_list', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_status', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='TodoList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_list', models.CharField(max_length=120)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='action',
            name='action_list',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='todo.TodoList'),
        ),
        migrations.AddField(
            model_name='action',
            name='action_status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todo.Status'),
        ),
        migrations.AddField(
            model_name='action',
            name='user',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
