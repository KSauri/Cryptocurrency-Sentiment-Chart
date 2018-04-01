from celery import Celery

app = Celery(
             'tasks',
             backend='redis://redis:6379/0',
             include=['application.tasks']
             )
app.conf.broker_url = 'redis://redis:6379/0'
