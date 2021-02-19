import pandas as pd
import sys
import argparse
import requests
import time


class CoinbaseMarketChecker:
    def __init__(self, args):
        self.args = args
        self.api_key = self.args.api_key
        self.time_interval = 5 * 60  # in seconds
        # this can be something a user can specify. (the type of crypto currency they would like to check)
        self.tickers_and_threshold = {'LTC': 228,'ETH': 2925,'ETC': 25, 'BTC': 80000}

    def get_crypto_price(self):
        crypto_info = {}
        for ticker in self.tickers_and_threshold.items():
            url = f'https://api.coinbase.com/v2/prices/{ticker[0]}-USD/buy'
            headers = {
                'Accepts': 'application/json',
                'X-CMC_PRO_API_KEY': self.api_key
            }

            # make a request to the coinmarketcap api
            response = requests.get(url, headers=headers)
            response_json = response.json()

            # extract the bitcoin price from the json data
            crypto_price = float(response_json['data']['amount'])
            crypto_info[ticker[0]] = crypto_price
        # I created this dataframe for my own purpose too kinda look at a more structured way to find ticker and prices.
        crypto_df = self.put_into_dataframe(crypto_info)
        print(crypto_df)
        return crypto_info



    def put_into_dataframe(self,dictionary):
        df = pd.DataFrame(list(dictionary.items()), columns=['Ticker', 'Price'])
        return df

    def continuous_crypto_checker(self):
        # this will be a infinite loop where we must put this specific function to sleep
        while True:
            crypto_price_dict = self.get_crypto_price()
            for item in crypto_price_dict.items():
                for threshold_num in self.tickers_and_threshold.items():
                    if (item[0] == threshold_num[0]) and item[1] > threshold_num[1]:
                        print('This is where we would send the notification')
                    else:
                        continue
            # this is where we sleep the function.
            time.sleep(600)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--api_key", type=str, default=None)
    parser.add_argument("--threshold", type=int, default=None)

    args = parser.parse_args()

    coinbasemarket = CoinbaseMarketChecker(args)
    coinbasemarket.continuous_crypto_checker()
