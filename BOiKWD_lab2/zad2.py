#  BOIKWD lab2
#  Katarzyna Nyznar
#  zadanie 2

import numpy as np
import numpy.linalg as npl

Cparam = np.matrix([[1, 5, 3, 4],
                    [1/5, 1, 4, 1],
                    [1/3, 1/4, 1, 2],
                    [1/4, 1, 1/2, 1]])

C1 = np.matrix([[1, 1/4, 2, 3],
                [4, 1, 5, 7],
                [1/2, 1/5, 1, 2],
                [1/3, 1/7, 1/2, 1]])

C2 = np.matrix([[1, 1, 4, 3],
                [1, 1, 4, 3],
                [1/4, 1/4, 1, 1/2],
                [1/3, 1/3, 2, 1]])

C3 = np.matrix([[1, 3, 1/2, 1/6],
                [1/3, 1, 1/3, 1/7],
                [2, 3, 1, 1/2],
                [6, 7, 2, 1]])

C4 = np.matrix([[1, 1/9, 1, 1/9],
                [9, 1, 9, 1],
                [1, 1/9, 1, 1/9],
                [9, 1, 9, 1]])


matrixList = [C1, C2, C3, C4]

normList = []
for m in matrixList:
    w = npl.eig(m)[1]  #wektory wlasne
    w = w[:,0]
    wNorm = abs(w) / sum(abs(w))
    print(wNorm)
    normList.append(wNorm)


wCparam = npl.eig(Cparam)[1]
wCparam = wCparam[:,0]
wCparamNorm = abs(wCparam) / sum(abs(wCparam))


it = 0
result = 0
for i in wCparamNorm:
    result += normList[it]*i
    it += 1

# print(result)
