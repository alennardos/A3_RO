import matplotlib.pyplot as plt
from math import sqrt
from random import random


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

