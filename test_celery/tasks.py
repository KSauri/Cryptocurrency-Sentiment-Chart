from crypto_currencies.get_data import CryptoCurrency
from datetime import datetime
from reddit.get_data import Reddit
from test_celery.celery import app


@app.task
def process_crypto_data():
    current_time = datetime.now()
    crypto = CryptoCurrency(current_time)
    response = crypto.get_data()
    return CryptoCurrency.process_data(response)


@app.task
def process_reddit_data():
    current_time = datetime.now()
    reddit = Reddit(current_time)
    return reddit.process_data()
