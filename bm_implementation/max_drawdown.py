import pandas as pd

portfolio_returns = pd.read_csv(
    "bm_implementation/portfolio_returns_rebalanced.csv",
    index_col=0,
    parse_dates=True
)

wealth = (1 + portfolio_returns).cumprod()
running_max = wealth.cummax()

drawdown = (wealth - running_max) / running_max

max_drawdown = drawdown.min()

pd.DataFrame(
    {"max_drawdown": [float(max_drawdown)]}
).to_csv("bm_implementation/max_drawdown.csv", index=False)

print("Max drawdown saved")