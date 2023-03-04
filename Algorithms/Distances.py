import math


def heuristic(a, b, distance="euclidienne"):
    if (distance == "euclidienne"):
        return euclidienne(a, b)
    if (distance == "manhattan"):
        return manhattan(a, b)
    if (distance == "tchebychev"):
        return tchebychev(a, b)


def euclidienne(a, b): return math.sqrt((b.i-a.i)**2 + (b.j-a.j)**2)


def manhattan(a, b): return (abs(b.i-a.i) + abs(b.j-a.j))


def tchebychev(a, b): return max(abs(b.i-a.i), abs(b.j-a.j))
