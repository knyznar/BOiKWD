# Katarzyna Nyznar
# zad2 BOiKWD lab7

from scipy.optimize import linprog

A = [[-5, -15],
     [-20, -5],
     [15, 2],
     [-1, 0],
     [0, -1]]

b = [-50, -40, 60, 0, 0]

c = [8, 4]

res = linprog(c, A, b)
resSteki = res.x[0]
resZiemniaki = res.x[1]
resMin = res.fun
print("Ilość steków: ", resSteki)
print("Ilość ziemniaków: ", resZiemniaki)
print("Minimalny koszt: ", resMin)
