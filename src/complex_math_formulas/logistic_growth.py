# https://medium.com/@ccpythonprogramming/converting-complex-mathematics-formulas-into-python-code-a-step-by-step-guide-baeac6b385d8
# 

import matplotlib.pyplot as plt
import math

def logistic_growth(initial_population: int, 
                    carrying_capacity:int, 
                    growth_rate:float, 
                    time_in_years:int) -> float:
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
    relative_difference = (carrying_capacity - initial_population) / initial_population
    exponential_decay_factor = math.exp(-growth_rate * time_in_years)
    return carrying_capacity / (1 + relative_difference * exponential_decay_factor)



# Example values
initial_population = 50  
carrying_capacity = 1000  
growth_rate = 0.1  
time_in_years = 10  

# growth = (logistic_growth(P0, K, r, t) for t in range(1,30))

# for t in range(1, 30):
#     growth = logistic_growth(P0, K, r, t)
#     print(f"Population after {t} years: {growth:.2f}")

# Generate values for t and corresponding population growth
years_range = range(1, 80)
growth_values = [logistic_growth(initial_population, carrying_capacity, 
                                 growth_rate, t) for t in years_range]

# Plot the result
plt.plot(years_range, growth_values, label='Logistic Growth')
plt.xlabel('Time (years)')
plt.ylabel('Population')
plt.title('Logistic Growth Model')
plt.legend()
plt.show()
