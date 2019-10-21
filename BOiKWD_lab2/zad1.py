#  BOIKWD lab2
#  Katarzyna Nyznar
#  zadanie 1

import numpy as np
import numpy.linalg as npl

C1 = np.matrix([[1, 1/7, 1/5], [7, 1, 3], [5, 1/3, 1]])
C2 = np.matrix([[1, 5, 9], [1/5, 1, 4], [1/9, 1/4, 1]])
C3 = np.matrix([[1, 4, 1/5], [1/4, 1, 1/9], [5, 9, 1]])
C4 = np.matrix([[1, 9, 4], [1/9, 1, 1/4], [1/4, 4, 1]])
C5 = np.matrix([[1,1,1], [1,1,1], [1,1,1]])
C6 = np.matrix([[1, 6, 4], [1/6, 1, 1/3], [1/4, 3, 1]])
C7 = np.matrix([[1, 9, 6], [1/9, 1, 1/4], [1/6, 3, 1]])
C8 = np.matrix([[1, 1/2, 1/2], [2, 1, 1], [2, 1, 1]])

matrixList = [C1, C2, C3, C4, C5, C6, C7, C8]

Cparam = np.array([[1,4,7,5,8,6,6,2],
                  [1/4,1,5,3,7,6,6,1/3],
                  [1/7,1/5,1,1/3,5,3,3,1/5],
                  [1/5,1/3,3,1,6,3,4,1/2],
                  [1/8,1/7,1/5,1/6,1,1/3,1/4,1/7],
                  [1/6,1/6,1/3,1/3,3,1,1/2,1/5],
                  [1/6,1/6,1/3,1/4,4,2,1,1/5],
                  [1/2,3,5,2,7,5,5,1]])

normList = []
for m in matrixList:
    w = npl.eig(m)[1]  #wektory wlasne
    w = w[:,0]
    wNorm = abs(w) / sum(abs(w))
    normList.append(wNorm)


wCparam = npl.eig(Cparam)[1]
wCparam = wCparam[:,0]
wCparamNorm = abs(wCparam) / sum(abs(wCparam))


it = 0
result = 0
for i in wCparamNorm:
    result += normList[it]*i
    it += 1

print(result)
