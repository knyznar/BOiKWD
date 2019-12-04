# Katarzyna Nyznar
# zad3 BOiKWD lab7

import numpy as np
from scipy.optimize import linprog

### GRACZ 1 ###

A = np.array([[0, 2, -3, 0],
            [-2, 0, 0, 3],
            [3, 0, 0, -4],
            [0, -3, 4, 0]])

min = np.min(A)
A += np.abs(min)

result = linprog([-1, -1, -1, -1], A, [1, 1, 1, 1], method='simplex')

v = 1/result.fun
v -= min

print ("GRACZ 1\nWartość gry: ", v)
print("Prawdopodobieństwa:")
print("1: ", result.x[0]/result.x.sum())
print("2: ", result.x[1]/result.x.sum())
print("3: ", result.x[2]/result.x.sum())
print("4: ", result.x[3]/result.x.sum())


### GRACZ 2 ###

A2 = np.array([[0, 2, -3, 0],
            [-2, 0, 0, 3],
            [3, 0, 0, -4],
            [0, -3, 4, 0]]).transpose()

min2 = np.min(A2)
A2 += np.abs(min2)
A2 *= (-1)
result2 = linprog([1, 1, 1, 1], A2, [-1, -1, -1, -1], method='simplex')

v2 = 1/result2.fun
v2 -= np.abs(min2)

print ("\nGRACZ 2\nWartość gry: ", v2)
print("Prawdopodobieństwa:")
print("1: ", result2.x[0]/result2.x.sum())
print("2: ", result2.x[1]/result2.x.sum())
print("3: ", result2.x[2]/result2.x.sum())
print("4: ", result2.x[3]/result2.x.sum())
