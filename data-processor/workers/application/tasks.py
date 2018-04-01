from application.celery import app
from crypto_currencies.get_data import CryptoCurrency
from datetime import datetime
from pymongo import MongoClient
from reddit.get_data import Reddit


client = MongoClient("mongodb://database:27017")
db = client['mongo']

# TODO check if this is kosher
reddit_collection = db.reddit_collection
crypto_collection = db.crypto_collection


@app.task
def process_crypto_data():
    current_time = datetime.now()
    crypto = CryptoCurrency(current_time)
    response = crypto.get_data()
    return crypto.process_data(response)


@app.task
def process_reddit_data():
    current_time = datetime.now()
    reddit = Reddit(current_time)
    # TODO you don't use get_data()
    return reddit.process_data()


@app.task
def save_data(data, collection_type):
    # TODO fix this
    if collection_type == "reddit":
        return str(reddit_collection.insert_one(data).inserted_id)
    else:
        return str(crypto_collection.insert_one(data).inserted_id)
