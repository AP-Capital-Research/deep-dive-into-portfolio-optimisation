import numpy as np
import pandas as pd

from src.backtesting.strategies import BlackLittermanStrategy


def dummy_view_builder(past_prices, decision_date):
    # No views at all for now
    P = np.zeros((0, past_prices.shape[1]))
    Q = np.zeros(0)
    return P, Q


def main():
    prices = pd.read_csv(
        "data/uk_multi_asset_prices_clean.csv",
        index_col=0,
        parse_dates=True,
    )

    market_weights = pd.Series(1.0 / prices.shape[1], index=prices.columns)

    def dummy_optimizer(mu, cov):
        return market_weights.copy()

    strat = BlackLittermanStrategy(
        market_weights=market_weights,
        risk_aversion=3.0,
        tau=0.05,
        view_builder=dummy_view_builder,
        optimizer=dummy_optimizer,
    )

    decision_date = prices.index[300]
    past_prices = prices.loc[:decision_date]
    weights = strat.get_target_weights(
        decision_date=decision_date,
        past_prices=past_prices,
        current_positions=pd.Series(0.0, index=prices.columns),
        cash=100_000.0,
    )

    print("Weights at", decision_date)
    print(weights)
    print("Sum of weights:", weights.sum())


if __name__ == "__main__":
    main()
