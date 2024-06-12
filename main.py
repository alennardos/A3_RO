import matplotlib.pyplot as plt
from math import sqrt
from random import random

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def arc(self, pointB, plt):
        if self != pointB:
            plt.plot((self.x, pointB.x), (self.y, pointB.y), marker = 'o')
            print(self.distance(pointB))

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
        return distanceTotal + pointsparc[-1].distance(depart)
    
    for p in points:
        if not p in pointsparc:
            tsp(p, points, distanceTotal, pointsparc)

print(tsp(points[0], points))

# for p in points:
#     p.sommet(plt)
#     points[5].arc(p, plt)

plt.show()