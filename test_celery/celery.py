from celery import Celery

app = Celery(
             'tasks',
             backend='mongodb://mongo:27017/0',
             include=['test_celery.tasks']
             )
app.conf.broker_url = 'redis://redis:6379/0'
