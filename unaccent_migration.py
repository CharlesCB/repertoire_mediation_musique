# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.db import migrations
from django.contrib.postgres.operations import UnaccentExtension

dependencies = [
        ('bdmultimedia', '0129_auto_20180709_1840'),
    ]

class Migration(migrations.Migration):
    operations = [ 
        UnaccentExtension(),
    ]