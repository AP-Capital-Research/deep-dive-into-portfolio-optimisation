import pandas as pd

portfolio_returns = pd.read_csv(
    "bm_implementation/portfolio_returns_rebalanced.csv",
    index_col=0,
    parse_dates=True
)

cumulative_returns = (1 + portfolio_returns).cumprod() - 1

cumulative_returns.to_csv("cumulative_returns.csv")

print("Cumulative returns saved")