import json
import requests

from ast import literal_eval


class CryptoCurrency:
    """
    CryptoCurrency relies on an API that returns the market cap for various crypto currencies

    The `get_data()` method returns data, including the market cap and current price, for the 25 largest
    crypto currencies

    The `process_data()` method returns a json string with data on the overall market cap
    as well as per coin data on price, rank, and market cap in USD
    """

    def __init__(self, timestamp):
        # TODO add check for timestamp type
        self.timestamp = timestamp

    def get_data(self):
        return requests.get('https://api.coinmarketcap.com/v1/ticker/?limit=25').content

    def process_data(self, crypto_data_response):
        price_data = crypto_data_response.decode()
        price_data = price_data.replace('null', 'None')
        price_data = literal_eval(price_data)

        final_price_data = {
            'market_cap': 0.0,
            'coins': [],
            'timestamp': self.timestamp
        }
        for coin in price_data:
            final_price_data['market_cap'] += float(coin['market_cap_usd'])
            final_price_data['coins'].append({
                'name': coin['name'],
                'price': coin['price_usd'],
                'rank': coin['rank'],
                'market_cap': coin['market_cap_usd']
            })

        return json.dumps(final_price_data)
