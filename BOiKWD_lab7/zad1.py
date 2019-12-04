# Katarzyna Nyznar
# zad1 BOiKWD lab7

from scipy.optimize import linprog

A = [[1, 1, 1],
     [-1, -1, -1],
     [-1, -2, -1],
     [0, 2, 1],
     [-1, 0, 0],
     [0, -1, 0],
     [0, 0, -1]]

b = [30, -30, -10, 20, 0, 0, 0]

c = [-2, -1, -3]

result = linprog(c, A, b).fun
result *= (-1)
print(round(result))
