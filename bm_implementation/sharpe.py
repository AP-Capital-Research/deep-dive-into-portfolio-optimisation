import pandas as pd
import numpy as np


portfolio_returns = pd.read_csv(
    "bm_implementation/portfolio_returns_rebalanced.csv",  
    index_col=0,                          
    parse_dates=True                     
)

risk_free_rate = 0.01

sharpe_ratio = (
    (portfolio_returns.mean() - risk_free_rate / 252)
    / portfolio_returns.std()
) * np.sqrt(252)

sharpe_df = pd.DataFrame(
    {"sharpe_ratio": [sharpe_ratio]}
)

pd.DataFrame(
    {"sharpe_ratio": [float(sharpe_ratio)]}
).to_csv("bm_implementation/sharpe_ratio.csv", index=False)

print("Sharpe ratio saved")