from __future__ import absolute_import
from test_celery.celery import app
import time
import requests
from pymongo import MongoClient
import redis


client = MongoClient('10.1.1.234', 27018)   # change the ip and port to your mongo database's
db = client.mongodb_test
collection = db.celery_test
post = db.test
print("mongo client established")
#
# redis_client = redis.Redis(
#                              host='redis',
#                              port=6379
#                            )
#
# redis_client.set('foo', 'bar')


@app.task()     # set a retry delay, 10 equal to 10s
def hello():
    return 'hello world'


@app.task(bind=True, default_retry_delay=10)     # set a retry delay, 10 equal to 10s
def longtime_add(self, i):
    print('long time task begins')
    print(redis_client.get('foo'))
    try:
        r = requests.get(i)
        # store status code and current time to mongodb
        post.insert({'status': r.status_code, "create_time": time.time()})
        print('long time task finished')
    except Exception as exc:
        raise self.retry(exc=exc)
    return r.status_code
