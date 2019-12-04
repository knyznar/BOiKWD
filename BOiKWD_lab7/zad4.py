# Katarzyna Nyznar
# zad4 BOiKWD lab7

import numpy as np
from scipy.optimize import linprog

### GRACZ 1 ###

A = np.array([[-2, 8, 2],
              [3, -1, 0]]).transpose()

min = np.min(A)
A = A + abs(min)
A *= (-1)

result = linprog([1, 1], A, [-1, -1, -1], method='simplex')
v = 1/result.fun
print("GRACZ 1:")
print("Wartość gry: ", v-abs(min))
print("Prawdopodobieństwa:")
print("1: ", result.x[0]/result.x.sum())
print("2: ", result.x[1]/result.x.sum())

### GRACZ 2 ###

A1 = np.array([[-2, 8, 2],
              [3, -1, 0]])

min1 = np.min(A1)
A1 = A1 + abs(min1)

result1 = linprog([-1, -1, -1], A1, [1, 1], method='simplex')
v = 1/result1.fun
print("\nGRACZ 2")
print("Wartość gry: ",v + min1)
print("Prawdopodobieństwa:")
print("1: ", result1.x[0]/result1.x.sum())
print("2: ", result1.x[1]/result1.x.sum())
print("3: ", result1.x[2]/result1.x.sum())
