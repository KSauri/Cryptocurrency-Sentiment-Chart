from celery import chain

from datetime import datetime
from application.celery import app
from crypto_currencies.get_data import CryptoPrices
from reddit.get_data import RedditCommentSentiment

CRYPTO = CryptoPrices()
REDDIT = RedditCommentSentiment()


@app.task
def save_crypto_data():
    data = CRYPTO.get()
    for coin in data['coins']:
        CRYPTO.save_coin_data(coin)
    CRYPTO.save_market_data(data['market'])
    return True


@app.task
def save_reddit_data():
    data = REDDIT.get()
    REDDIT.save(data)
    return True

@app.task
def master_task():
    save_crypto_data.delay()
    save_reddit_data.delay()
    return True