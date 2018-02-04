from celery import chain
from .tasks import process_crypto_data, process_reddit_data, save_data, REDDIT_COLLECTION, CRYPTO_COLLECTION


if __name__ == '__main__':
    res1 = chain(process_reddit_data.s(), save_data.s("reddit"))()
    res2 = chain(process_crypto_data.s(), save_data.s("crypto"))()
    res1.get()
    res2.get()
