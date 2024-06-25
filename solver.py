from pulp import *
import random
from math import sqrt
import matplotlib.pyplot as plt

liste = [(25, 11), (22, 24), (25, 6), (28, 27), (24, 22), (16, 2), (26, 1), (5, 22), (3, 19), (13, 9)]

# for i in range(10):
#     liste.append((random.randint(0, 30), random.randint(0, 30)))


def calculeDistance(val):
    return sqrt((val[0][0] - val[1][0])**2  + (val[0][1] - val[1][1])**2)

prob = LpProblem("MonPb", LpMinimize)


x = LpVariable.dicts('objects', [(liste[i],liste[j]) for i in range(len(liste)) for j in range(i+1, len(liste))]
                             ,lowBound = 0
                             ,upBound = 1
                             ,cat = 'Binary'
                             )


prob += lpSum([calculeDistance((liste[i],liste[j]))*x[(liste[i],liste[j])] for i in range(len(liste)) for j in range(i+1, len(liste))])

for i in range(len(liste)):
    prob += lpSum([x[(liste[i],liste[j])] for j in range(len(liste)) if (liste[i],liste[j]) in x.keys()]) + lpSum([x[(liste[j],liste[i])] for j in range(len(liste)) if (liste[j],liste[i]) in x.keys()]) == 2

for i in range(len(liste)):
    for j in range(i, len(liste)):
        if (liste[i],liste[j]) in x.keys():
            for k in range(j, len(liste)):
                if (liste[i],liste[k]) in x.keys() and (liste[j],liste[k]) in x.keys():
                    prob += x[liste[i],liste[j]] + x[liste[i],liste[k]] + x[liste[j],liste[k]] <= 2

prob.solve()

print(LpStatus[prob.status])
print("Min=", value(prob.objective))

print("Valeur: " + str(value(prob.objective)))
for i in range(len(liste)):
    for j in range(i+1, len(liste)):
        if x[liste[i],liste[j]].value() == 1.0:
            plt.plot((liste[i][0], liste[j][0]), (liste[i][1], liste[j][1]), marker = 'o')

plt.show()