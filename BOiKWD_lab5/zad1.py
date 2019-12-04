# Katarzyna Nyznar
# lab 5 BOiKWD

import numpy as np

A = np.array([[1,2/3,2,5/2,5/3,5],
              [3/2,1,3,10/3,3,9],
              [1/2,1/3,1,4/3,7/8,5/2],
              [2/5,3/10,3/4,1,5/6,12/5],
              [3/5,1/3,8/7,6/5,1,3],
              [1/5,1/9,2/5,5/12,1/3,1]])

B = np.array([[1,2/5,3,7/3,1/2,1,2],
              [5/2,1,4/7,1,1,3,2/3],
              [1/3,7/4,1,1/2,2,1/2,1],
              [3/7,1,2,1,4,2,6],
              [2,1,1/2,1/4,1,1/2,3/4],
              [1,1/3,2,1/2,2,1,5/8],
              [1/2,3/2,1,1/6,4/3,8/5,1]])

C = np.array([[1,2/3,2/15,1,8,12/5,1,1/2],
              [3/2,1,1,2,1,2/3,1/6,1],
              [15/2,1,1,5/2,7/8,2,1,1/5],
              [1,1/2,2/5,1,4/3,1,2/7,1],
              [1/8,1,8/7,3/4,1,1/5,2/7,1],
              [5/12,3/2,1/2,1,5,1,3,2],
              [1,6,1,7/2,7/2,1/3,1,3/11],
              [2,1,5,1,1,1/2,11/3,1]])

D = np.array([[0,1,1,-1,-1,1,-1],
              [-1,0,0,1,1,-1,0],
              [-1,0,0,0,1,1,-1],
              [1,-1,0,0,1,0,1],
              [1,0,-1,-1,0,1,-1],
              [-1,1,-1,1,-1,0,0],
              [1,0,1,-1,1,0,0]])

E = np.array([[0,1,0,0,-1],
              [-1,0,0,0,1],
              [0,0,0,1,0],
              [0,0,-1,0,0],
              [1,-1,0,0,0]])

F = np.array([[0,-1,1,-1,1,-1,1,-1,1],
              [1,0,1,1,1,-1,-1,-1,-1],
              [-1,-1,0,-1,1,-1,1,1,1],
              [1,-1,1,0,-1,1,-1,1,-1],
              [-1,-1,-1,1,0,-1,1,1,1],
              [1,1,1,-1,1,0,-1,-1,-1],
              [-1,1,-1,1,-1,1,0,1,-1],
              [1,1,-1,-1,-1,1,-1,0,1],
              [-1,1,-1,1,-1,1,1,-1,0]])

def macierzTurniejowa(M):
    X = np.empty([len(M), len(M)], dtype=int)
    for i in range(len(M)):
        for j in range(len(M)):
            if M[i][j] == 1:
                X[i][j] = 0
            elif M[i][j] > 1:
                X[i][j] = 1
            elif M[i][j] < 1:
                X[i][j] = -1
    return X


def czyTurniejowa(M):
    for i in range(len(M)):
        for j in range(i+1):
            if i == j and M[i][j] != 0:
                return False
            if M[i][j] != -M[j][i]:
                return False
            elif M[i][j] != 1 and M[i][j] != -1 and M[i][j] != 0:
                return False
    return True

def znajdzRemisy(M):
    for i in range(len(M)):
        for j in range(len(M)):
            if i != j and M[i][j] == 0:
                return True
    return False


def indeksKendala(M):
    licznik = 0
    n = len(M)
    for i in range(n):
        for j in range(i):
            for k in range(j):
                if i != j and j != k and k != i and M[i][j] == M[j][k] == M[k][i]:      # mij = mjk = mki
                    licznik += 1
    if n % 2 != 0:      # jeśli n nieparzyste
        maxLicznik = (n**3 - n)/24
    else:               # jeśli n parzyste
        maxLicznik = (n**3 - 4*n)/24
    return 1 - (licznik/maxLicznik)


def indeksKendalaUogolniony(M):
    licznik = 0
    n = len(M)
    for i in range(n):
        for j in range(i):
            for k in range(j):
                if i != j and j != k and k != i:
                    if M[i][j]==M[j][k]==0 and M[k][i]!=0 or M[i][j]==M[k][i]==0 and M[j][k]!=0 or M[j][k]==M[k][i]==0 and M[i][j]!=0:
                        licznik += 1
                    elif M[i][j]==M[j][k]!=0 and M[k][i]==0 or M[i][j]==M[k][i]!=0 and M[j][k]==0 or M[j][k]==M[k][i]!=0 and M[i][j]==0:
                        licznik += 1
                    elif M[i][j] == M[j][k] == M[k][i] != 0:
                        licznik += 1
    if n%4 == 0:
        maxLicznik = (13*n**3 - 24*n**2 - 16*n)/96
    elif n%4 == 1:
        maxLicznik = (13*n**3 - 24*n**2 - 19*n + 30)/96
    elif n%4 == 2:
        maxLicznik = (13*n**3 - 24*n**2 - 4*n)/96
    elif n%4 == 3:
        maxLicznik = (13*n**3 - 24*n**2 - 19*n + 18)/96
    return 1 - (licznik/maxLicznik)


Aturniejowa = macierzTurniejowa(A)
Bturniejowa = macierzTurniejowa(B)
Cturniejowa = macierzTurniejowa(C)
print(Aturniejowa)
print(Bturniejowa)
print(Cturniejowa)

if czyTurniejowa(D):
    print("Macierz D jest uogólniona turniejowa")
if czyTurniejowa(E):
    print("Macierz E jest uogólniona turniejowa")
if czyTurniejowa(F):
    print("Macierz F jest uogólniona turniejowa")

if znajdzRemisy(Aturniejowa):
    print("Macierz A dopuszcza remisy")
if znajdzRemisy(Bturniejowa):
    print("Macierz B dopuszcza remisy")
if znajdzRemisy(Cturniejowa):
    print("Macierz C dopuszcza remisy")
if znajdzRemisy(E):
    print("Macierz E dopuszcza remisy")
if znajdzRemisy(F):
    print("Macierz F dopuszcza remisy")

print("\nUogólnione indeksy Kendala:")
print("macierz A: ", indeksKendalaUogolniony(Aturniejowa))
print("macierz B: ", indeksKendalaUogolniony(Bturniejowa))
print("macierz C: ", indeksKendalaUogolniony(Cturniejowa))
print("macierz E: ", indeksKendalaUogolniony(E))
print("macierz F: ", indeksKendalaUogolniony(F))
print("\nKlasyczne indeksy Kendala:")
print("macierz A: ", indeksKendala(Aturniejowa))
print("macierz F: ", indeksKendala(F))
