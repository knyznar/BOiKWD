#  BOIKWD lab2
#  Katarzyna Nyznar
#  zadanie 3


import numpy as np
import numpy.linalg as npl

cena = np.matrix([[1, 1/5, 3],
                [5, 1, 7],
                [1/3, 1/7, 1]])

zuzyciePaliwa = np.matrix([[1, 2, 1/3],
                        [1/2, 1, 1/5],
                        [3, 5, 1]])

bezpieczenstwo = np.matrix([[1, 3, 1/2],
                            [1/3, 1, 1/4],
                            [2, 4, 1]])

bagaznik = np.matrix([[1, 4, 3],
                    [1/4, 1, 1/2],
                    [1/3, 2, 1]])

pasazerowie = np.matrix([[1, 1, 4],
                        [1, 1, 4],
                        [1/4, 1/4, 1]])

Cc = np.array([[1, 3],  # macierz porownan podkategorii ceny (cena samochodu i zuzycie paliwa)
               [1/3, 1]])

Cp = np.array([[1, 1/5],  # macierz porownan podkategorii pojemnosci (wielkosc bagaznika i liczba pasazerow)
               [5, 1]])

Cparam = np.array([[1, 1/6, 3],  # macierz porownan kategorii
                [6, 1, 8],
                [1/3, 1/8, 1]])

matrixList = [cena, zuzyciePaliwa, bezpieczenstwo, bagaznik, pasazerowie]

normList = []
for m in matrixList:
    w = npl.eig(m)[1]  #wektory wlasne
    w = w[:,0]
    wNorm = abs(w) / sum(abs(w))
    normList.append(wNorm)

wCc = npl.eig(Cc)[1]
wCc = wCc[:,0]
wCcNorm = abs(wCc) / sum(abs(wCc))  #waga ceny samochodu i zuzycia paliwa

wCp = npl.eig(Cp)[1]
wCp = wCp[:,0]
wCpNorm = abs(wCp) / sum(abs(wCp))  #waga wielkosci bagaznika i liczby pasazerow


wCparam = npl.eig(Cparam)[1]
wCparam = wCparam[:,0]
wCparamNorm = abs(wCparam) / sum(abs(wCparam))  #wagi kategorii (cena, bezpieczenstwo, pojemnosc)
print(wCparamNorm)
#ranking kategorii:
ranking = np.array([wCcNorm[0]*wCparamNorm[0],
                    wCcNorm[1]*wCparamNorm[0],
                    wCparamNorm[1],
                    wCpNorm[0]*wCparamNorm[2],
                    wCpNorm[1]*wCparamNorm[2]])


wektoryWlasneNorm = np.concatenate(normList, axis=1)

result = wektoryWlasneNorm.dot(ranking)
# print(result)
