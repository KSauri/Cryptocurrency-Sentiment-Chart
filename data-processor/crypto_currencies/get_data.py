from datetime import datetime
from pymongo import MongoClient
import requests

from ast import literal_eval


class CryptoPrices:
    """
    CryptoPrices relies on an API that returns the market cap for various crypto currencies

    The `get()` method returns a json string with data on the overall market cap
    as well as per coin data on price, rank, and market cap in USD
    """

    def _get_data(self):
        mongo_client =  MongoClient('mongodb://mongo:27017/mongo')
        db = mongo_client.mongo
        self._coin_collection = db.coinprices
        self._market_collection = db.marketprices
        return requests.get('https://api.coinmarketcap.com/v1/ticker/?limit=25').content

    def _process_prices(self, crypto_data_response, timestamp):
        price_data = crypto_data_response.decode()
        price_data = price_data.replace('null', 'None')
        price_data = literal_eval(price_data)

        final_price_data = {
            'market': {
                'market_cap': 0.0,
                'timestamp': str(timestamp)
            },
            'coins': [],
        }
        for coin in price_data:
            final_price_data['market']['market_cap'] += float(coin['market_cap_usd'])
            final_price_data['coins'].append({
                'name': coin['name'],
                'price': coin['price_usd'],
                'rank': coin['rank'],
                'market_cap': coin['market_cap_usd'],
                'timestamp': str(timestamp)
            })

        return final_price_data
    
    def get(self):
        """
        `get()` will fetch name, price, rank, and market cap data for the top 25 crypto currencies.

        Args:
            None required.

        Returns:
            dict: a dictionary containing information about the top 25 crypto currencies
        """
        timestamp = datetime.now()
        data = self._get_data()
        return self._process_prices(data, timestamp)

    def save_coin_data(self, coin_data):
        self._coin_collection.insert_one(coin_data)
        return True
        
    def save_market_data(self, market_data):
        self._market_collection.insert_one(market_data)
        return True