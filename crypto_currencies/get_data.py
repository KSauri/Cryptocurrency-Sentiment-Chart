import datetime
import json
import requests

from ast import literal_eval

# TODO obviously fix all this

# One function to get the list of all currencies
# And another that uses 'sched' to make a call every 3 minutes
# How do I keep track of the last time that coin's price was called?


class CryptoCurrency:

    def get_data(self):
        return requests.get('https://api.coinmarketcap.com/v1/ticker/?limit=25').content

    def process_data(self, crypto_data_response, timestamp):
        price_data = crypto_data_response.decode()
        price_data = price_data.replace('null', 'None')
        price_data = literal_eval(price_data)

        final_price_data = {
            'market_cap': 0.0,
            'coins': []
        }
        for coin in price_data:
            final_price_data['market_cap'] += float(coin['market_cap_usd'])
            final_price_data['coins'].append({
                'name': coin['name'],
                'price': coin['price_usd'],
                'rank': coin['rank'],
                'market_cap': coin['market_cap_usd']
            })

        return final_price_data
