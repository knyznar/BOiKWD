#  BOIKWD lab3
#  Katarzyna Nyznar
#  zadanie 2

import numpy as np
import numpy.linalg as npl
import math


def Satty(A):
    values = npl.eig(A)[0]
    realValues = np.isreal(values)
    for i in range(values.size):
        if realValues[i] is False:
            values[i] = 0
    maxVal = np.real(np.max(values))
    return (maxVal-len(A))/(len(A)-1)


def getRanking(A):
    result = []
    for W in A:
        W = np.squeeze(np.asarray(W))
        result.append(W.prod() ** (1.0 / len(W)))
    result = abs(np.asarray(result)) / sum(abs(np.asarray(result)))
    return result


def Geom(A):
    ranking = getRanking(A)
    n = len(A)
    sum = 0
    for i in range(1, n):
        for j in range(i+1, n):
            sum += (math.log(A[i][j] * ranking[j]/ranking[i], 10)) ** 2
    return (2/((n-1)*(n-2)))*sum


def Koczkodaj(A):
  result = []

  for i in range(len(A)):
    for j in range(len(A)):
      for k in range(len(A)):
        a = abs(1 - (A[i][k] * A[k][j]) / A[i][j])
        b = abs(1 - A[i][j] / (A[i][k] * A[k][j]))
        result.append(min(a,b))
  return max(result)


A = [[1,7,3], [1/7,1,2], [1/3,1/2,1]]
B = [[1,1/5,7,1], [5,1,1/2,2], [1/7,2,1,3], [1,1/2,1/3,1]]
C = [[1,2,5,1,7], [1/2,1,3,1/2,5], [1/5,1/3,1,1/5,2], [1,2,5,1,7], [1/7,1/5,1/2,1/7,1]]

print("Indeks spójności Sattego:")
print(Satty(A))
print(Satty(B))
print(Satty(C))
print("\nIndeks spójności geometryczny")
print(Geom(A))
print(Geom(B))
print(Geom(C))
print("\nIndeks spójności Koczkodaja:")
print(Koczkodaj(A))
print(Koczkodaj(B))
print(Koczkodaj(C))
