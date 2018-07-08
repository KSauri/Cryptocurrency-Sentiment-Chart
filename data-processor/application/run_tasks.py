from .tasks import save_crypto_data, save_reddit_data


if __name__ == '__main__':
    # use delay, not get
    save_crypto_data.delay()
    save_reddit_data.delay()
