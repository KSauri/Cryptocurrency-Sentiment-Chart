FROM python:3.6
ADD requirements.txt /app/
ADD ./test_celery/ /app/
WORKDIR /app
ADD . /app
RUN pip install -r requirements.txt
ENTRYPOINT celery -A test_celery worker --loglevel=info
