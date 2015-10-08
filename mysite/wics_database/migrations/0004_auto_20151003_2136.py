# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wics_database', '0003_auto_20151003_1749'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wicsmember',
            name='yearInCollege',
            field=models.CharField(choices=[('1U', '1st Year Undergrad'), ('2U', '2nd Year Undergrad'), ('3U', '3rd Year Undergrad'), ('4U', '4th Year Undergrad'), ('5U', '5th Year Undergrad'), ('U++', '5+th Year Undergrad'), ('GR', 'Graduate')], max_length=3),
        ),
    ]
