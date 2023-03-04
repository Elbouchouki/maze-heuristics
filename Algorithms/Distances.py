from Params import minkowski_p
from math import *
from decimal import Decimal


def heuristic(a, b, distance="euclidienne"):
    if (distance == "euclidienne"):
        return euclidienne(a, b)
    if (distance == "manhattan"):
        return manhattan(a, b)
    if (distance == "tchebychev"):
        return tchebychev(a, b)
    if (distance == "minkowski"):
        return minkowski_distance(a, b, minkowski_p)


def euclidienne(a, b): return sqrt((b.i-a.i)**2 + (b.j-a.j)**2)


def manhattan(a, b): return (abs(b.i-a.i) + abs(b.j-a.j))


def tchebychev(a, b): return max(abs(b.i-a.i), abs(b.j-a.j))


def p_root(value, root):
    root_value = 1 / float(root)
    return round(value ** root_value, 3)


def minkowski_distance(a, b, p_value):
    return (p_root((pow(abs(b.i-a.i), p_value) + pow(abs(b.j-a.j), p_value)), p_value))
