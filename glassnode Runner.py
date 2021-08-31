# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas.core.frame import DataFrame
import seaborn as sns
import plotly.graph_objects as go

from glassnode import GlassnodeClient, Indicators, Market, Mining, Supply, Addresses,Transactions,Blockchain,Derivatives,Distribution,Entities,Institutions, URLS
from tqdm import tqdm

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

GLASSNODE_API_KEY = '1vUcyF35hTk9awbNGszF0KcLuYH'

self = GlassnodeClient()
self.set_api_key(GLASSNODE_API_KEY)


Metrics = {'Indicators':Indicators,
           'Market':Market,
           'Mining':Mining,
           'Supply':Supply,
           'Addresses':Addresses,
           'Transactions':Transactions,
           'Blockchain':Blockchain,
           'Derivatives':Derivatives,
           'Distribution':Distribution,
           'Entities':Entities,
           'Institutions':Institutions}


DataDict = {}
series = {}
dataframes = {}
catalog = {}

for group in Metrics:
    DataDict[group] = {}
    series[group] = []
    dataframes[group] = []
    catalog[group] = []
# %%
for group in tqdm(list(Metrics.keys())):
    
    metric = Metrics[group]

    for m in metric:
        df = pd.DataFrame()
        
        url = URLS[group] + m
        a ='BTC'
        c = 'native'
        i='24h'

        df = self.get(url,a,i,c)
        
        if isinstance(df,pd.DataFrame):
            dataframes[group].append(m)
        else:
            series[group].append(m)
            
        DataDict[group][m] = df
        
        try:
            start_date = df.index[0].strftime('%Y-%m-%d')
            end_date = df.index[-1].strftime('%Y-%m-%d')
            
            if isinstance(df,pd.DataFrame):
                N_NaNs = df.iloc[:,0].isna().sum()
            else:
                N_NaNs = df.isna().sum()
                
        except:
            start_date,end_date,N_NaNs
            
        catalog[group].append({'Name':m,'start_date':start_date,'end_date':end_date,'N_NaNs':N_NaNs})
        
    catalog[group] = pd.DataFrame(catalog[group])
# %%
