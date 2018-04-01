from celery import chain
from .tasks import process_crypto_data, process_reddit_data


if __name__ == '__main__':
    chain(process_crypto_data.s())().get()
    chain(process_reddit_data.s())().get()
