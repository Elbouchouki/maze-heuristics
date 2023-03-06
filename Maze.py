from Graphics import *
import math
import random
from Algorithms import astar, heuristic
from Params import *
from PIL import Image
import numpy as np


class Spot:
    def __init__(self, i, j, cols, rows):
        self.i = i
        self.j = j

        self.cols = cols
        self.rows = rows
        # f, g, and h values for A*
        self.f = None  # g cost + h cost
        self.g = None  # distance from starting node
        self.h = None  # heuristic, distance from end node
        self.shape = None

        # Neighbors
        self.neighbors = None
        self.neighboringWalls = None

        self.Parent = None

        self.isWall = False

    def show(self, win, color):
        if self.shape:
            self.shape.setFill(color)

        else:
            self.shape = Rectangle(
                Point(self.i*height/self.rows, self.j*width/self.cols), Point((self.i+1)*height/self.rows, (self.j+1)*width/self.cols))
            self.shape.setFill(color)
            self.shape.draw(win)

    def addNeighbors(self, grid):
        self.neighbors = []
        self.neighboringWalls = []

        if self.j < self.cols-1:
            self.neighbors.append(grid[self.i][self.j+1])
            if self.i > 0:
                self.neighbors.append(grid[self.i-1][self.j+1])
            if self.i < self.rows-1:
                self.neighbors.append(grid[self.i+1][self.j+1])

        if self.j > 0:
            self.neighbors.append(grid[self.i][self.j-1])
            if self.i > 0:
                self.neighbors.append(grid[self.i-1][self.j-1])
            if self.i < self.rows-1:
                self.neighbors.append(grid[self.i+1][self.j-1])

        if self.i > 0:
            self.neighbors.append(grid[self.i-1][self.j])
        if self.i < self.rows-1:
            self.neighbors.append(grid[self.i+1][self.j])


def init_grid():
    grid = [[Spot(i, j, cols=cols, rows=rows)
             for j in range(cols)] for i in range(rows)]
    for i in range(rows):
        for j in range(cols):
            grid[i][j].addNeighbors(grid)
    # add walls to grid
    for j in range(cols):
        for i in range(rows):
            if random.randint(0, 100) < WallPercentage:
                grid[i][j].isWall = True
    return grid


def init_test(grid):
    StartNode = grid[0][0]
    EndNode = grid[len(grid)-1][len(grid[0])-1]
    StartNode.isWall = False
    EndNode.isWall = False
    return grid, [], [], StartNode, EndNode


def imageToGrid(img: str):
    temp = Image.open(img)
    temp = temp.convert('1')
    A = np.array(temp)
    # (A.shape[0], A.shape[1])
    rows = len(A)
    cols = len(A[0])

    grid = [[Spot(i, j, cols=cols, rows=rows)
             for j in range(cols)] for i in range(rows)]

    for i in range(rows):
        for j in range(cols):
            grid[i][j].addNeighbors(grid)
    # add walls to grid
    for j in range(cols):
        for i in range(rows):
            if A[i][j] == False:
                grid[i][j].isWall = True
    return grid
