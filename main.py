import matplotlib.pyplot as plt
from math import sqrt
from random import random
from pulp import *

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.voision = []

    def arc(self, pointB, plt):
        if self != pointB:
            plt.plot((self.x, pointB.x), (self.y, pointB.y), marker = 'o')

    def sommet(self, plt):
        plt.plot(self.x, self.y,'o')
    
    def distance(self, pointB):
        return sqrt((self.x - pointB.x)**2  + (self.y - pointB.y)**2)

points = []

# voisin = []

for i in range(10):
    points.append(Point(x=random()*10, y=random()*10))

def tsp(depart, points, distanceTotal = 0, pointsparc = []):
    pointsparc.append(depart)
    if len(pointsparc) == 10:
        return (distanceTotal + pointsparc[-2].distance(depart), pointsparc)
    
    min = 1000000000000
    voisin = None
    for p in points:
        if not p in pointsparc:
            distance = depart.distance(p)
            if distance < min:
                min = distance
                voisin = p
    
    return tsp(voisin, points, distanceTotal+distance, pointsparc)

res = tsp(points[0], points)

distance = res[0]

for i in range(len(res[1])-1):
    res[1][i].sommet(plt)
    res[1][i].arc(res[1][i+1], plt)

res[1][0].arc(res[1][-1], plt)

print(distance)

# for p in points:
#     p.sommet(plt)
#     points[5].arc(p, plt)

plt.show()

AB = LpVariable("AB", 0, 1, const.LpBinary)
AC = LpVariable("AC", 0, 1, const.LpBinary)
AD = LpVariable("AD", 0, 1, const.LpBinary)
AE = LpVariable("AE", 0, 1, const.LpBinary)

BC = LpVariable("BC", 0, 1, const.LpBinary)
BD = LpVariable("BD", 0, 1, const.LpBinary)
BE = LpVariable("BE", 0, 1, const.LpBinary)

CD = LpVariable("CD", 0, 1, const.LpBinary)
CE = LpVariable("CE", 0, 1, const.LpBinary)

DE = LpVariable("DE", 0, 1, const.LpBinary)

# probleme
prob = LpProblem("choix", LpMinimize)

# objectif
prob += AB + AC + AD + AE == 2
prob += AB + BC + BD + BE == 2
prob += AC + BC + CD + CE == 2
prob += AE + BE + CE + DE == 2
prob += AD + BD + CD + DE == 2

# contrainte
prob += 10*AB + 2*AC + 3*AD + 4*AE + 1*BC + 5*BD + 30*BE + 5*CD + 8*CE + 9*DE

prob.solve()
print("a")
print(LpStatus[prob.status])
print("Min=", value(prob.objective))

# variables resultat
for v in prob.variables():
    print("%s=%.2f"%(v.name,v.varValue), end=', ')