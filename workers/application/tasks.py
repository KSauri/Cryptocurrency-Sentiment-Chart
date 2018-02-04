from application.celery import app
from crypto_currencies.get_data import CryptoCurrency
from datetime import datetime
from pymongo import MongoClient
from reddit.get_data import Reddit


client = MongoClient("mongodb://database:27017")
db = client['mongo']

REDDIT_COLLECTION = db.reddit_collection
CRYPTO_COLLECTION = db.crypto_collection


@app.task
def process_crypto_data():
    current_time = datetime.now()
    print("executing crypto task")
    crypto = CryptoCurrency(current_time)
    response = crypto.get_data()
    return crypto.process_data(response)


@app.task
def process_reddit_data():
    current_time = datetime.now()
    reddit = Reddit(current_time)
    return reddit.process_data()


@app.task
def save_data(data, collection_type):
    if collection_type == "reddit":
        return str(REDDIT_COLLECTION.insert_one(data).inserted_id)
    else:
        return str(CRYPTO_COLLECTION.insert_one(data).inserted_id)
