# ---
# jupyter:
#   jupytext:
#     formats: py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.11.5
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

import pandas as pd
import numpy as np
import seaborn as sns
import plotly.graph_objects as go


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


