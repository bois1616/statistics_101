# https://medium.com/@ccpythonprogramming/converting-complex-mathematics-formulas-into-python-code-a-step-by-step-guide-baeac6b385d8
# https://towardsdatascience.com/logistic-growth-model-6d8d2d4e5d6c
# 

import matplotlib.pyplot as plt
import math

def logistic_growth(P0: int, K:int, r:float, t:int) -> float:
    """
    Calculate the population growth using the logistic growth model.
    P(t) = K / (1 + ((K - P0) / P0) * e^(-rt))
    P(t) = population at time t
    P0 = initial population
    K = carrying capacity
    r = growth rate
    t = time in years
    e = Euler's number
    """
    return K / (1 + ((K - P0) / P0) * math.exp(-r * t))



# Example values
P0 = 50  # Initial population
K = 1000  # Carrying capacity
r = 0.1   # Growth rate
t = 10    # Time in years

growth = (logistic_growth(P0, K, r, t) for t in range(1,30))

# for t in range(1, 30):
#     growth = logistic_growth(P0, K, r, t)
#     print(f"Population after {t} years: {growth:.2f}")

# Generate values for t and corresponding population growth
t_values = range(1, 30)
growth_values = [logistic_growth(P0, K, r, t) for t in t_values]

# Plot the result
plt.plot(t_values, growth_values, label='Logistic Growth')
plt.xlabel('Time (years)')
plt.ylabel('Population')
plt.title('Logistic Growth Model')
plt.legend()
plt.show()
