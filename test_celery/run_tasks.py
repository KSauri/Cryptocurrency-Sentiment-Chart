from .tasks import process_crypto_data, process_reddit_data
import time


if __name__ == '__main__':
    result = process_crypto_data.delay()
    print('Task finished?', result.ready())
    print('Task result:', result.result)
    time.sleep(10)
    print('Task finished"', result.ready())
    print('Task result:', result.result)
