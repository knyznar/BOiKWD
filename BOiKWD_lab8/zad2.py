# Katarzyna Nyznar
# lab8
# zadanie 2

import numpy as np
from scipy.optimize import linprog

A = np.array([[0.5, 0.4, 0.4, 0.2],
              [0.4, 0.2, 0, 0.5]]).transpose()
A *= -1

B = np.array([2000, 2800])

C = np.array([10, 14, 8, 11])
C *= -1

result = linprog(B, A, C)
for i in result.x:
    print(round(i))
print("Wynik funkcji celu: ", round(result.fun))
print()


A1 = []
C1 = []
indexC = 0
for i in A:
    if indexC >= len(C):
        break
    if abs(i[0])*result.x[0] + abs(i[1])*result.x[1] <= abs(C[indexC]):
        C1.append(C[indexC])
        A1.append([abs(i[0]), abs(i[1])])
    else:
        print("Usunięto indeks ", indexC)
    indexC += 1

print("Nowa macierz A:")
print(A1)
print("Nowy wektor C:")
print(C1)

result1 = linprog(C1, A1, B)
print("\nA = 0")
print("B = ", round(result1.x[0]))
print("C = 0")
print("D = ", round(result1.x[1]))

print("Wynik funkcji celu: ", round(-result1.fun))

