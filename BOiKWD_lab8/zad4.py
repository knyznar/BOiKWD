# Katarzyna Nyznar
# lab8
# zadanie 4

from scipy.optimize import linprog
import numpy as np

A = np.array([[2, 2, 1, 1, 1, 0, 0, 0, 0],  # 11cm
              [1, 0, 2, 1, 0, 3, 2, 1, 0],  # 8cm
              [0, 1, 0, 2, 3, 1, 2, 4, 6]])  # 5cm

b = np.array([12000, 24000, 27000])
c = np.array([0, 3, 3, 1, 4, 1, 4, 2, 0])

Adualna = A.transpose() * (-1)
Bdualna = c * (-1)
Cdualna = b

result = linprog(Cdualna, Adualna, Bdualna)
print(result.x)
print("Wartość funkcji celu:", result.fun)

A1 = []
C1 = []
indexB = 0
for i in Adualna:
    if indexB >= len(Bdualna):
        break
    if abs(i[0])*result.x[0] + abs(i[1])*result.x[1] + abs(i[2])*result.x[2] <= abs(Bdualna[indexB]):
        C1.append(Bdualna[indexB])
        A1.append([abs(i[0]), abs(i[1]), abs(i[2])])
    else:
        print("Usunięto indeks ", indexB+1)
    indexB += 1

A1 = np.asarray(A1).transpose()
C1 = np.asarray(C1)
print("Nowa macierz A:")
print(A1)
print("Nowy wektor C:")
print(C1)

result1 = linprog(C1, A1, b)
print("Wynik:", -result1.fun)
