from pulp import *
import random
from math import sqrt
import matplotlib.pyplot as plt

liste = [(25, 11), (22, 24), (25, 6), (28, 27), (24, 22), (16, 2), (26, 1), (5, 22), (3, 19), (13, 9), (28, 23), (28, 1), (27, 13), (4, 28), (12, 7), (18, 6), (23, 17), (27, 2), (14, 2), (0, 30), (1,1), (2,2), (3,3)]

# for i in range(10):
#     liste.append((random.randint(0, 30), random.randint(0, 30)))


def calculeDistance(val):
    return sqrt((val[0][0] - val[1][0])**2  + (val[0][1] - val[1][1])**2)

prob = LpProblem("MonPb", LpMinimize)

nbCamion = 1

x = LpVariable.dicts('objects', [(c, liste[i],liste[j]) for i in range(len(liste)) for j in range(i+1, len(liste)) for c in range(nbCamion)]
                             ,lowBound = 0
                             ,upBound = 1
                             ,cat = 'Integer'
                             )


prob += lpSum([calculeDistance((liste[i],liste[j]))*x[(c, liste[i],liste[j])] for i in range(len(liste)) for j in range(i+1, len(liste)) for c in range(nbCamion)])

for i in range(len(liste)):
    prob += lpSum([x[(c, liste[i],liste[j])] for j in range(len(liste)) for c in range(nbCamion) if (c, liste[i],liste[j]) in x.keys()]) + lpSum([x[(c, liste[j],liste[i])] for j in range(len(liste)) for c in range(nbCamion) if (c, liste[j],liste[i]) in x.keys()]) == 2

def funct(res, prob):
    prob += lpSum([x[(c, res[i],res[j])] for i in range(len(res)) for j in range(len(res)) for c in range(nbCamion) if (c, res[i],res[j]) in x.keys()]) <= len(res)-1

def constListe(n, point, res, boucle, prob):
    res.append(point)
    if len(res) == n:
        funct(res, prob)
    else:
        for p in range(boucle, len(liste)):
            if (liste[p] not in res):
                boucle+=1
                constListe(n, liste[p], res.copy(), boucle, prob)

print("start")
for i in range(3, 7):
    j = 1
    for p in liste:
        constListe(i, p, [], j, prob)
        j+=1

prob.solve()

print(LpStatus[prob.status])
print("Min=", value(prob.objective))

colors = ["black", "blue", "red"]

print("Valeur: " + str(value(prob.objective)))
for c in range(nbCamion):
    for i in range(len(liste)):
        for j in range(i+1, len(liste)):
            if x[c, liste[i],liste[j]].value() == 1.0:
                plt.plot((liste[i][0], liste[j][0]), (liste[i][1], liste[j][1]), marker = 'o', color = colors[c])
            print(c, liste[i], liste[j], x[c,liste[i],liste[j]].value())

plt.show()