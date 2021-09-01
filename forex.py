# %%
import pandas as pd
import numpy as np
import talib as ta
import pickle
import matplotlib.pyplot as plt
import seaborn as sns

sns.set()
# %%
with open('/Users/orentapiero/Data/Mid5T.pickle', 'rb') as handle:
    Mid = pickle.load(handle)

# %%
pair = 'gbpusd'
date = '2018-02-27'
ohlc = Mid[pair].loc[date].dropna()

# %%
open = ohlc['open']
high = ohlc['high']
low = ohlc['low']
close = ohlc['close']

real = ta.APO(close, fastperiod=12, slowperiod=24, matype=0)

f,a = plt.subplots(nrows = 2,sharex = True)
close.plot(ax=a[0])
real.plot(ax = a[1])
# %%

