# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 13:10:07 2019

@author: 17101538
"""
import pandas as pd
#import numpy as np
import matplotlib.pyplot as plt

p=pd.read_csv('StockPriceData.csv',delimiter=',')

p[['Adj Close']].plot()
p[['Adj Close']].rolling(100).mean().plot()
q= p[['Adj Close']].rolling(100).mean()
#p['m']=q
print(p.head(20))
n=p.dropna()
p.plot()

plt.show()