FROM python:3.6
ADD requirements.txt /app/requirements.txt
ADD ./test_celery/ /app/
WORKDIR /app
ADD . /app
RUN pip install -r requirements.txt
ENTRYPOINT celery -A test_celery worker --loglevel=info
#ENTRYPOINT ['celery','-A','test_celery', 'worker', '--loglevel=info']
