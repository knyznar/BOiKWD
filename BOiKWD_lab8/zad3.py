# Katarzyna Nyznar
# lab8
# zadanie 3

from scipy.optimize import linprog
import numpy as np

A = np.array([[4, 1, 8, 5, 2, 0],
              [0, 1, 0, 1, 2, 3]])
B = np.array([12000, 18000])
C = np.array([0.1, 0.2, 0.2, 0.3, 0.4, 0])

Adualna = A.transpose()
Cdualna = B * (-1)
Bdualna = C

result = linprog(Cdualna, Adualna, Bdualna)

print("Wyniki:")
for i in result.x:
    print(i)
print("Wartość funkcji celu:", result.fun * (-1))

A1 = []
C1 = []
indexB = 0
for i in Adualna:
    if indexB >= len(Bdualna):
        break
    if abs(i[0])*result.x[0] + abs(i[1])*result.x[1] >= abs(Bdualna[indexB]):
        C1.append(Bdualna[indexB])
        A1.append([abs(i[0]), abs(i[1])])
    else:
        print("Usunięto indeks ", indexB+1)
    indexB += 1

A1 = np.asarray(A1).transpose()
print("Nowa macierz A:")
print(A1)
print("Nowy wektor C:")
print(C1)

print("\nx2 = 0")
print("x4 = 0")
print("x5 = 0")

print("Z pozostałych zmiennych powstaje układ równań:")
print("4x1 + 8x3 = 12000")
print("3x6 = 18000")
print("Zatem rozwiązań jest nieskończenie wiele: x6 = 6000 oraz pary x1 + 2x3 = 3000")



