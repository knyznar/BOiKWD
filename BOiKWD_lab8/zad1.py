# Katarzyna Nyznar
# lab8
# zadanie 1

from scipy.optimize import linprog
import numpy as np

A = np.asarray([[1, 3, 2, 3, 1],
                [4, 6, 5, 7, 1]])

B = np.asarray([6, 15])
C = np.asarray([2, 5, 3, 4, 1])

Adualna = A.transpose() * (-1)
Bdualna = C * (-1)
Cdualna = B

result = linprog(Cdualna, Adualna, Bdualna)
print(result)
print("\nWynik: ", result.fun)
