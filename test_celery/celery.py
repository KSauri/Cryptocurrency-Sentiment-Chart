from __future__ import absolute_import
from celery import Celery


app = Celery(
             'tasks',
             backend='rpc://',
             include=['test_celery.tasks']
             )
app.conf.broker_url = 'redis://redis:6379/0'
