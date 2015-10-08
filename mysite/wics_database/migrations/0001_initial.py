# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='wicsMember',
            fields=[
                ('firstName', models.CharField(max_length=50)),
                ('lastName', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50, serialize=False, primary_key=True)),
                ('yearInCollege', models.IntegerField()),
                ('major', models.CharField(max_length=50, choices=[(b'1U', b'1st Year Undergrad'), (b'2U', b'2nd Year Undergrad'), (b'3U', b'3rd Year Undergrad'), (b'4U', b'4th Year Undergrad'), (b'5U', b'5th Year Undergrad'), (b'U++', b'5+th Year Undergrad'), (b'GR', b'Graduate')])),
                ('mostRecentMeetingDate', models.CharField(max_length=50)),
                ('numMeetingsAttended', models.IntegerField(default=0)),
                ('identifiedGender', models.CharField(max_length=50)),
            ],
        ),
    ]
