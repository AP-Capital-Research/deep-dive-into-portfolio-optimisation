import numpy as np
import pandas as pd

return_matrix = pd.read_csv(
    "bm_implementation/return_matrix.csv",
    index_col=0,
    parse_dates=True
)

def compute_mean_cov(return_matrix):
    mu = return_matrix.mean()
    Sigma = return_matrix.cov()
    return mu, Sigma

if __name__ == "__main__":
    mu, Sigma = compute_mean_cov(return_matrix)
    mu.to_csv("bm_implementation/mean_returns.csv", header=["mean_return"])
    Sigma.to_csv("bm_implementation/covariance_matrix.csv")
