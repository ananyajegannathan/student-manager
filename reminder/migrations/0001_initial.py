# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-12 11:43
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
            name='Reminder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=50)),
                ('event_date', models.DateField()),
                ('freq', models.CharField(choices=[(b'o', b'Once'), (b'd', b'Daily'), (b'w', b'Weekly'), (b'm', b'Monthly'), (b'y', b'Yearly')], max_length=1, verbose_name=b'Frequency')),
                ('reminder_date', models.DateField(help_text=b'You will start receiving reminders from this date at the chosen frequency.')),
                ('time', models.TimeField(verbose_name=b'Time to send reminder')),
                ('extra_text', models.CharField(blank=True, max_length=500, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reminders', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
