import pandas as pd
import numpy as np

portfolio_returns = pd.read_csv(
    "bm_implementation/portfolio_returns_rebalanced.csv",
    index_col=0,
    parse_dates=True
)

daily_vol = portfolio_returns.std().iloc[0]
annual_vol = daily_vol * np.sqrt(252)

pd.DataFrame(
    {"daily_volatility": [daily_vol]}
).to_csv("bm_implementation/daily_volatility.csv", index=False)

pd.DataFrame(
    {"annual_volatility": [annual_vol]}
).to_csv("bm_implementation/annual_volatility.csv", index=False)

print("Daily and annual volatility saved")