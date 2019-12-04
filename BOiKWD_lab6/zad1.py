import numpy as np

M = np.array([[20, -150, -250],
              [150, -80, -100],
              [250, 100, 40]])

def minimax(A):
    minVec = []
    maxVec = []
    for i in range(len(A)):
        for j in range(len(A)):
            tempMin = A[i][j]
            tempMax = A[j][i]
            if A[j][i] > tempMax:
                tempMax = A[j][i]
            if A[i][j] < tempMin:
                tempMin = A[i][j]
        minVec.append(tempMin)
        maxVec.append(tempMax)
    minVal = max(minVec)
    maxVal = min(maxVec)

    if minVal == maxVal:
        return minVal
    else:
        print("Brak rozwiązania")


print(minimax(M))