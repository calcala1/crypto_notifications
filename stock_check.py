import pandas as pd
import sys
import argparse
import time
from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.cryptocurrencies import CryptoCurrencies

class CheckingStockPrice:
    def __init__(self, args):
        self.args = args
        #self.ts = TimeSeries(key=self.args.api_key, output_format='pandas')
        self.cc = CryptoCurrencies(key=self.args.api_key, output_format='pandas')
        self.daily_data, self.meta_data = self.cc.get_digital_currency_daily(symbol='ETC', market='USD')
        print('reached here')
        # pass

    def get_excel_sheet(self):
        i = 1
        while i is 1:
            self.data.to_excel('/Users/christianalcala/desktop/microsoft.xlsx')
            time.sleep(60)

        #close_data





if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--api_key", type=str, default=None)
    args = parser.parse_args()

    stock_check = CheckingStockPrice(args)
    stock_check.get_excel_sheet()
