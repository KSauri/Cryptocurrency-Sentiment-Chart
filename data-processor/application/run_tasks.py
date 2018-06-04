from celery import chain

from .tasks import process_crypto_data, process_reddit_data, save_crypto_data, save_reddit_data


if __name__ == '__main__':
    # use delay, not get
    chain(process_crypto_data.s(), save_crypto_data.s()).delay()
    chain(process_reddit_data.s(), save_reddit_data.s()).delay()
