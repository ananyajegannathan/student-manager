# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-19 07:42
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reminder', '0004_attendance'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(choices=[(1, b'Male'), (2, b'Female')], default=2, max_length=64)),
                ('phone_no', models.BigIntegerField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='reminder',
            name='user',
        ),
        migrations.AddField(
            model_name='item',
            name='extra_notes',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='item_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='set_reminder',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='item',
            name='time',
            field=models.TimeField(blank=True, null=True, verbose_name=b'Time to send reminder'),
        ),
        migrations.AlterField(
            model_name='item',
            name='is_completed',
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name='Reminder',
        ),
    ]