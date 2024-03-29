"""Russian Peasant Multiplication"""
import math
import pandas as pd

# Setting n1 as the smaller number typically results in a faster calculation
n1 = 18
n2 = 89

halving = [n1]

while min(halving) > 1:
    halving.append(math.floor(min(halving) / 2))

doubling = [n2]

while len(doubling) < len(halving):
    doubling.append(max(doubling) * 2)

half_double = pd.DataFrame(zip(halving, doubling))

half_double = half_double.loc[half_double[0] % 2 == 1, :]
answer = sum(half_double.loc[:, 1])
print(answer)
