# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wics_database', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wicsmember',
            name='major',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='wicsmember',
            name='yearInCollege',
            field=models.IntegerField(choices=[(b'1U', b'1st Year Undergrad'), (b'2U', b'2nd Year Undergrad'), (b'3U', b'3rd Year Undergrad'), (b'4U', b'4th Year Undergrad'), (b'5U', b'5th Year Undergrad'), (b'U++', b'5+th Year Undergrad'), (b'GR', b'Graduate')]),
        ),
    ]
