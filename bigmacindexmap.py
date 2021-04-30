#!/usr/bin/env python
# coding: utf-8

# In[150]:


import numpy as np
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
from ipywidgets import interact, interactive, fixed, interact_manual
import ipywidgets as widgets


# In[93]:


ds = pd.read_csv("big-mac-full-index.csv")
dates = ds.date.unique()
cc = plt.colormaps()


# In[75]:


def prep_table(inp):
    path = gpd.datasets.get_path('naturalearth_lowres')
    df = gpd.read_file(path)
    df["BMI"]=df.iso_a3.copy()
    dds = ds[ds.date==inp][["iso_a3","USD_raw"]]
    chg={}
    for i in df.iso_a3:
        for j in dds.iso_a3:
            if i==j:
                chg.update( {i : dds[dds.iso_a3==j].USD_raw.values[0]})
    for i in df[~df.iso_a3.isin(dds.iso_a3)].iso_a3.values:
        chg.update( {i : np.nan})
    df["BMI"] = df["BMI"].replace(chg)
    return df


# In[76]:


date_=dates[0]
fig, ax = plt.subplots(figsize=(24,18))
df.plot(ax=ax, alpha=0.4, color='grey')
prep_table(date_).plot(column='BMI', ax=ax, legend=True, legend_kwds={'shrink': 0.53})
plt.title('BigMacIndex from '+date_)


# In[170]:


get_ipython().run_line_magic('matplotlib', 'inline')
get_ipython().run_line_magic('config', 'InlineBackend.close_figures=True')
    
def f(Date,Color="Spectral"):
    date_=dates[Date]
    cc_=Color
    fig, ax = plt.subplots(figsize=(24,18))
    df.plot(ax=ax, alpha=0.4, color='grey')
    prep_table(date_).plot(column='BMI', ax=ax, legend=True,cmap=cc_, legend_kwds={'shrink': 0.53})
    plt.title('BigMacIndex from '+date_)
    return Date,Color

widgets.interact(f, Date=(0,len(dates)-1),Color=cc)


# In[ ]:




