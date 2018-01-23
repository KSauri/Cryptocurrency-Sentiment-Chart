import datetime

from pymongo import MongoClient
from .tasks import process_crypto_data, process_reddit_data

client = MongoClient("mongodb://database:27017")
db = client['mongo']

REDDIT_COLLECTION = db.reddit_collection
CRYPTO_COLLECTION = db.crypto_collection


if __name__ == '__main__':
    process_reddit_data.delay()
    process_crypto_data.delay()
    # print('Task finished?', result.ready())
    # print('Task result:', result.result)
    # time.sleep(301)
    # print('Task finished"', result.ready())
    # print('Task result:', result.result)
