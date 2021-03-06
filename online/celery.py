#!/usr/bin/env python
# -*-coding=utf-8-*-
from __future__ import unicode_literals, absolute_import

import os
import django

from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'online.settings')
django.setup()
BROKER_URL = 'redis://redis:6379/0'
BACKEND_URL = 'redis://redis:6379/1'

app = Celery('online', broker=BROKER_URL)
app.conf.result_backend = BACKEND_URL

app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)