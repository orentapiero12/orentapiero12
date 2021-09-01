#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import yfinance as yf
import talib as ta

from tqdm import tqdm
sns.set()
#%%
def fwd_return(Px, L):
    fwd = Px.shift(-L)
    ret = 10000 * np.log(fwd / Px)
    ret.name = 'F' + str(L) + 'ret'
    return ret

def ta_pattern_fit(hist, L, candle_pattern):
    expression = 'ta.' + candle_pattern + '(hist.Open,hist.High,hist.Low,hist.Close)'
    patt = eval(expression)
    patt.name = candle_pattern
    Fret = fwd_return(hist['Close'], L)
    df = pd.concat([patt, Fret], axis=1).dropna()

    avg = df.groupby(candle_pattern)[Fret.name].agg({'mean', 'std', 'count'})

    Npos = df.groupby(candle_pattern)[Fret.name].apply(lambda x: x[x > 0].count())
    Npos.name = 'Npos'

    AW = df.groupby(candle_pattern)[Fret.name].apply(lambda x: x[x > 0].mean())
    AL = df.groupby(candle_pattern)[Fret.name].apply(lambda x: x[x < 0].mean())

    AW.name = 'AW'
    AL.name = 'AL'

    summary = pd.concat([avg, Npos, AW, AL], axis=1)
    summary['hit_ratio'] = summary['Npos'] / summary['count']

    return summary
#%%
ticker = yf.Ticker("GBPUSD=X")
hist = ticker.history(period="max")
#%%
L = 5
PATTERNS = ta.get_function_groups()['Pattern Recognition']

for patt in PATTERNS:
    summary = ta_pattern_fit(hist.loc[:'2020'],L,patt)
    display(summary[['mean','AW','AL','hit_ratio','count']])
# %%
