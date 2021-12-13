# -*- coding: utf-8 -*-
"""
Created on Sun Dec 12 21:10:57 2021

@author: beile.yaaqob.aisin
"""

import pandas_datareader as web
import pandas as pd
import datetime as dt

path = 'C://Users/beile.yaaqob.aisin/Downloads/The_Reddit_Ethereum_Dataset/'

start = dt.datetime(2016,5,15) # arbitrary begining date of the last market cycle
end = dt.datetime(2021,11,1) #end date of the eth reddit dataset

eth = web.DataReader('ETH-USD', 'yahoo', start, end)
btc = web.DataReader('BTC-USD', 'yahoo', start, end)

eth.to_csv(path+'eth_price.csv')
btc.to_csv(path+'btc_price.csv')