# BigMacIndexMap

## Preview

![](https://raw.githubusercontent.com/ambader/BigMacIndexMap/main/BIM_Map.gif)

## Get Data

Data from ![The Economist](https://www.economist.com/big-mac-index)\
Obtained .csv from ![Kaggle](https://www.kaggle.com/paultimothymooney/the-economists-big-mac-index)

## How to use
```python
date_=dates[0]
fig, ax = plt.subplots(figsize=(24,18))
df.plot(ax=ax, alpha=0.4, color='grey')
prep_table(date_).plot(column='BMI', ax=ax, legend=True, legend_kwds={'shrink': 0.53})
plt.title('BigMacIndex from '+date_)
```
![](https://www.kaggleusercontent.com/kf/60989555/eyJhbGciOiJkaXIiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2In0..VkZNOImkHsjEbswuU6zHxA.mJWRfAzUEgvRHjLaaRtgIWSSrByZP0We5T_aIKi9OnrdOJLC5yA6DgxEkhWG6Cgv7yck90azXxY1jfOrvvzPevkBK7ZF6t_EekanJ00WlRbjwwcqvWl-mACFkuiSl4Fw_dUVMw9KxBU1NYvYOjjrmjfeU_eJqgokw-5O5dGSBMWKhV-_rm3p4uE1v4XwHlUNmlH6K4GHIcEcHtvmhRokOtEVYX_isWGpErpAuUJK84XttD0bHCctq8nmTlL7gaqcyTO3XnRnnT9gf4RKxEpjfR5nkE6HlQ5dRRWINuYu4NYEF1SGmyeq6Wc-WnihVe3z0O0v85sdZef84wcw4gGxY7jwSuUYEJ8bzDjoQaemnI73B1Fxm4dlHdbh0xkZWf8qfYvDJ3Rx6dAyKVFnCLk1ajFDrfWSfsKSkN4w3q3J9hrj4yyumLNQnlxTLXVemrG88ouTwbpVDFQ-mk5eFDx-3_-ABl0YYsigMBXxu-0TBrYpoV15It_WrQ20qufHtu-hSr5rTWWVvWR41Q8Y6xC2pm9tq0uZbwd15uXM1mu3lhP_mxSEQJwr-9hjeDo50GCr6fUg7fPwt1hqpm0TFoZNVMXimcuQHYnsQPc9n8hLXfa4gt5GYKfNRhAVbgz2WM5mmZkDNnP3IkN2exLcTRkdzjgHC8JLna0_I-DNAwiegTA.6Cera0wBE2YrPhGMwQxg2A/__results___files/__results___4_1.png)
