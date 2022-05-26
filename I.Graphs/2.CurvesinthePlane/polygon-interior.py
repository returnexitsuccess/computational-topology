#!/usr/bin/python3

# Determine whether a point is in the interior of a simple polygon


def det(x, a, b):
    # 1, x1, x2
    # 1, a1, a2
    # 1, b1, b2
    return (a[0] * b[1] - b[0] * a[1]
          + b[0] * x[1] - x[0] * b[1]
          + x[0] * a[1] - a[0] * x[1])

class Polygon():
    def __init__(self, vertexList):
        self.vertexList = vertexList

    def isInterior(self, x, y):
        numCrossings = 0
        for i in range(len(self.vertexList)):
            a = self.vertexList[i]
            b = self.vertexList[(i + 1) % len(self.vertexList)]
            if self.doesCross((x, y), a, b):
                numCrossings += 1

        return (numCrossings % 2 != 0)

    def doesCross(self, x, a, b):
        if a[1] < b[1]:
            if a[1] <= x[1] and x[1] < b[1]:
                return det(x, a, b) > 0
            else:
                return False
        elif a[1] > b[1]:
            if b[1] <= x[1] and x[1] < a[1]:
                return det(x, b, a) > 0
            else:
                return False
        else:
            return False


# comb polygon taken from https://people.sc.fsu.edu/~jburkardt/datasets/polygon/polygon.html
comb = Polygon([
    (8, 0),
    (7, 10),
    (6, 0),
    (5, 10),
    (4, 0),
    (3, 10),
    (2, 0),
    (1, 10),
    (0, 0),
    (4, -2)
])

testPoints = [
    (0, 10),  # False
    (2, 4),   # False
    (1, -1),  # False
    (7, -1),  # False
    (4, -1),  # True
    (1, 4),   # True
    (7, 8),   # True
    (1, 0)    # True
]

for pt in testPoints:
    print(f"{pt} is interior? {comb.isInterior(pt[0], pt[1])}")
