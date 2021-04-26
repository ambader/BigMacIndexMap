# BigMacIndexMap

Data from ![The Economist](https://www.economist.com/big-mac-index)
Obtained .csv from ![Kaggle](https://www.kaggle.com/paultimothymooney/the-economists-big-mac-index)

## How to use
```python
date_=dates[0]
fig, ax = plt.subplots(figsize=(24,18))
df.plot(ax=ax, alpha=0.4, color='grey')
prep_table(date_).plot(column='BMI', ax=ax, legend=True, legend_kwds={'shrink': 0.53})
plt.title('BigMacIndex from '+date_)
```
