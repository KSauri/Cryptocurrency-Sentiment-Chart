from celery import Celery

app = Celery(
    'tasks',
    include=['application.tasks']
)
app.conf.broker_url = 'redis://redis:6379/0'
app.conf.beat_schedule = {
    'master': {
        'task': 'application.tasks.master_task',
        'schedule': 300.0,
    },
}
app.conf.timezone = 'UTC'