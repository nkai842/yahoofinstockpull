import pandas_datareader as pdr
from datetime import datetime, date, timedelta
from yahoo_fin import stock_info as si
import numpy as np


class DataYahoo():
    def __init__(self,ticker):
        self.today = date.today()
        self.ticker = ticker
    def pull_data(self):
        ## Retrieves 1 week of stock data from yahoo finance
        tick = pdr.get_data_yahoo(symbols = self.ticker, start=self.today - timedelta(days = 7), end=self.today - timedelta(days = 1))
        return tick
    def plot(self):
        ## Plots the adjusted close price of stocks over 1 week
        tick = pdr.get_data_yahoo(symbols=str(self.ticker), start=self.today - timedelta(days = 7), end=self.today - timedelta(days = 1))
        tick['Adj Close'].plot(grid = False)
        plt.show()
    def pivot_calc(self):
        tick = pdr.get_data_yahoo(symbols=str(self.ticker), start=self.today - timedelta(days = 1), end=self.today - timedelta(days = 1))
        pp = (tick['High'] + tick['Low'] + tick['Open']) / 3
        R1 = (2*pp) - tick['Low']
        S1 = (2*pp) - tick['High']
        R2 = pp + (tick['High'] - tick['Low'])
        S2 = pp - (tick['High'] - tick['Low'])
        R3 = tick['High'] + 2*(pp - tick['Low'])
        S3 = tick['Low'] - 2*(tick['High'] - pp)
