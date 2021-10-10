# %%
import pandas as pd
import numpy as np
import talib as ta
import pickle
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go

sns.set()
# %%
def ohlc_plot(df,start = '2018',end = '2021',Log = False):
    if Log:
        fig = go.Figure(data=[go.Candlestick(x=df.loc[start:end].index,
                        open=np.log(df.Open.loc[start:end]),
                        high=np.log(df.High.loc[start:end]),
                        low=np.log(df.Low.loc[start:end]),
                        close=np.log(df.Close.loc[start:end]))])
    else:
        fig = go.Figure(data=[go.Candlestick(x=df.loc[start:end].index,
                        open=(df.Open.loc[start:end]),
                        high=(df.High.loc[start:end]),
                        low=(df.Low.loc[start:end]),
                        close=(df.Close.loc[start:end]))])


    fig.update_layout(xaxis_rangeslider_visible=False)
    fig.show()
    return

# %%
with open('/Users/orentapiero/Data/Mid5T.pickle', 'rb') as handle:
    Mid = pickle.load(handle)
    
with open('/Users/orentapiero/Data/Bid5T.pickle', 'rb') as handle:
    Bid = pickle.load(handle)

with open('/Users/orentapiero/Data/Ask5T.pickle', 'rb') as handle:
    Ask = pickle.load(handle)

# %%
pair = 'gbpusd'
date = '2018'
ohlc = Mid[pair].loc[date].dropna()
ohlc.columns = ['Open','High','Low','Close']

# %%
ohlc_plot(ohlc,start = '2018-02-26',end = '2018-02-26',Log = False)

# %%
ohlc['H30mCmx'] = ohlc['Close'].rolling(6).max()
ohlc['H30mCmn'] = ohlc['Close'].rolling(6).min()

ohlc['H60mCmx'] = ohlc['Close'].rolling(12).max()
ohlc['H60mCmn'] = ohlc['Close'].rolling(12).min()

ohlc['H150mCmx'] = ohlc['Close'].rolling(30).max()
ohlc['H150mCmn'] = ohlc['Close'].rolling(30).min()


# %%
ohlc.loc['2018-02-26',('H30mCmx','H30mCmn')].between_time('07:00','12:00').plot(figsize = (18,10),style = 'k--')
ohlc.loc['2018-02-26',('H60mCmx','H60mCmn')].between_time('07:00','12:00').plot(figsize = (18,10),style = 'b--')
ohlc.loc['2018-02-26',('H150mCmx','H150mCmn')].between_time('07:00','12:00').plot(figsize = (18,10),style = 'r--')

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


# %%
