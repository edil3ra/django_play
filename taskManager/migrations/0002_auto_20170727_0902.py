# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-27 09:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('taskManager', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeveloperWorkTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_elapsed_dev', models.IntegerField(blank=True, default=None, null=True, verbose_name='Time elapsed')),
                ('developer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='taskManager.Developer')),
            ],
        ),
        migrations.RemoveField(
            model_name='task',
            name='app_user',
        ),
        migrations.AddField(
            model_name='developerworktask',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='taskManager.Task'),
        ),
        migrations.AddField(
            model_name='developer',
            name='tasks',
            field=models.ManyToManyField(through='taskManager.DeveloperWorkTask', to='taskManager.Task'),
        ),
        migrations.AddField(
            model_name='task',
            name='developers',
            field=models.ManyToManyField(through='taskManager.DeveloperWorkTask', to='taskManager.Developer'),
        ),
    ]