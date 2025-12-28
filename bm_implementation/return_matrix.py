import pandas as pd

price_df = pd.read_csv(
    "price_matrix.csv",
    index_col=0,
    parse_dates=True
)
return_df = price_df.pct_change().dropna()
return_df.to_csv("return_matrix.csv")
print("Return matrix shape:", return_df.shape)

print(return_df.isna().sum().sum())
