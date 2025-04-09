import math
from scipy.stats import norm

# Black-Scholes function to calculate call option price
def black_scholes_call(CurrentStockPrice: float,
                       StrikePrice: float,
                       TimeToMaturity: int,
                       risk_free_rate: float,
                       volatility: float) -> float:
    """
    Calculates a call option price using the Black-Scholes formula.
    C = S0 * N(d1) - X * exp(-r * T) * N(d2), where:
    N: Cumulative distribution function of the standard normal distribution
    S0: Current stock price
    X: Strike price
    T: Time to maturity (in years)
    r: Risk-free interest rate
    sigma: Volatility, or standard deviation of the stock returns
    d1 = (ln(S0/X) + (r + 0.5 * sigma^2) * T) / (sigma * sqrt(T))
    d2 = d1 - sigma * sqrt(T)
    """
    d1 = (math.log(CurrentStockPrice / StrikePrice) +
          (risk_free_rate + 0.5 * volatility ** 2) * TimeToMaturity) /
    (volatility * math.sqrt(TimeToMaturity))
    d2 = d1 - volatility * math.sqrt(TimeToMaturity)
    call_price = CurrentStockPrice * norm.cdf(d1) - StrikePrice * math.exp(-risk_free_rate * TimeToMaturity) * norm.cdf(d2)
    return call_price

# Example values
S0 = 100  # Current stock price
X = 95    # Strike price
T = 1     # Time to maturity (1 year)
r = 0.05  # Risk-free interest rate
sigma = 0.2  # Volatility

print(f"Call Option Price: {black_scholes_call(S0, X, T, r, sigma):.2f}")
