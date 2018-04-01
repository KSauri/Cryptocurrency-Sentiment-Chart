FROM python:3.6
ADD requirements.txt /app/
ADD . /app
WORKDIR /app
RUN pip install -r requirements.txt
RUN python -m nltk.downloader vader_lexicon

ENTRYPOINT celery -A application worker --loglevel=info
