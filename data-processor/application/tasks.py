from celery import chain

from datetime import datetime
from application.celery import app
from crypto_currencies.get_data import CryptoPrices
from reddit.get_data import RedditCommentSentiment

CRYPTO = CryptoPrices()
REDDIT = RedditCommentSentiment()


@app.task
def process_crypto_data():
    return CRYPTO.get()


@app.task
def process_reddit_data():
    return REDDIT.get()


@app.task
def save_crypto_data(data):
    for coin in data['coins']:
        CRYPTO.save_coin_data(coin)
    CRYPTO.save_market_data(data['market'])
    return True


@app.task
def save_reddit_data(data):
    REDDIT.save(data)
    return True

@app.task
def master_task():
    chain(process_crypto_data.s(), save_crypto_data.s()).delay()
    chain(process_reddit_data.s(), save_reddit_data.s()).delay()
    return True