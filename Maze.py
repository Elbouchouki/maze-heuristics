import numpy as np
from Graphics import *
import math
import pandas as pd
import random
from Algorithms import astar, heuristic
from Params import *


class Spot:
    def __init__(self, i, j):
        # Location
        self.i = i
        self.j = j
        # self.width=width
        # self.height=height

        # f, g, and h values for A*
        self.f = None  # g cost + h cost
        self.g = None  # distance from starting node
        self.h = None  # heuristic, distance from end node
        self.shape = None

        # Neighbors
        self.neighbors = None
        self.neighboringWalls = None

        # Where did I come from?
        self.Parent = None

        # Am I a wall?
        self.isWall = False

    def show(self, win, color):
        if self.shape:
            self.shape.setFill(color)

        else:
            # self.shape = Circle(Point(self.i*w,self.j*h), 10)
            self.shape = Rectangle(
                Point(self.i*w, self.j*h), Point((self.i+1)*w, (self.j+1)*h))
            # self.shape.setOutline("blue")
            self.shape.setFill(color)
            self.shape.draw(win)

    def addNeighbors(self, grid):
        self.neighbors = []
        self.neighboringWalls = []

        if self.j < cols-1:
            self.neighbors.append(grid[self.i][self.j+1])
            if self.i > 0:
                self.neighbors.append(grid[self.i-1][self.j+1])
            if self.i < rows-1:
                self.neighbors.append(grid[self.i+1][self.j+1])

        if self.j > 0:
            self.neighbors.append(grid[self.i][self.j-1])
            if self.i > 0:
                self.neighbors.append(grid[self.i-1][self.j-1])
            if self.i < rows-1:
                self.neighbors.append(grid[self.i+1][self.j-1])

        if self.i > 0:
            self.neighbors.append(grid[self.i-1][self.j])
        if self.i < rows-1:
            self.neighbors.append(grid[self.i+1][self.j])


# def get_best_heuristic(OpenSet):
#     winner_index = 0
#     for i in range(len(OpenSet)):
#         if OpenSet[i].f < OpenSet[winner_index].f:
#             winner_index = i
#     return OpenSet[winner_index]


def init_grid():
    grid = [[Spot(i, j) for j in range(cols)] for i in range(rows)]
    for i in range(rows):
        for j in range(cols):
            grid[i][j].addNeighbors(grid)
    # add walls to grid
    for j in range(cols):
        for i in range(rows):
            if random.randint(0, 100) < WallPercentage:
                grid[i][j].isWall = True
    return grid


def init_test(grid=init_grid()):
    StartNode = grid[0][0]
    EndNode = grid[rows-1][cols-1]
    StartNode.isWall = False
    EndNode.isWall = False
    return grid, [], [], StartNode, EndNode


# def draw_path(StartNode, EndNode, win, DrawGrid):
#     if DrawGrid:
#         StartNode.show(win, 'yellow')
#         EndNode.show(win, 'yellow')
#         update(changeRate)

#     previous = EndNode.Parent
#     ContinueSearch = True
#     solutionLength = 2

#     while ContinueSearch:
#         solutionLength = solutionLength+1
#         if DrawGrid:
#             previous.show(win, 'yellow')
#             update(changeRate)
#         previous = previous.Parent
#         if previous == StartNode:
#             ContinueSearch = False

#     return solutionLength


# def astar(OpenSet, ClosedSet, StartNode, EndNode, grid, win, DrawGrid=True, distanceType="euclidienne"):
#     OpenSet.append(StartNode)
#     ContinueSearch = True
#     iLoop = 1
#     # Step1 -  Start the loop to find the best solution
#     while ContinueSearch:

#         CurrentNode = get_best_heuristic(OpenSet)

#         # Step 2b remove current node from open list
#         OpenSet.remove(CurrentNode)

#         # Step 2c add current node to closed list
#         ClosedSet.append(CurrentNode)

#         # Step 2d if current node is target node we found optimal path and exit loop
#         if CurrentNode == EndNode:
#             ContinueSearch = False

#         # Step 2e for each neighbor in the current node
#         for i in range(len(CurrentNode.neighbors)):

#             # Step 2e-1 if:neigbor is not traversable or neighbor in closed goto next neighbor
#             if (CurrentNode.neighbors[i] not in ClosedSet) and (CurrentNode.neighbors[i].isWall == False):
#                 # set tentative gscore to gscore(current)+dist(current,neightbor)

#                 # Step 2e-2 else: if (new_path to neighbor is shorter) or (neigbor is not in openlist)

#                 if (CurrentNode.neighbors[i] not in ClosedSet):
#                     # use heuristic function for determing stepsize
#                     tempG = CurrentNode.g + \
#                         heuristic(
#                             CurrentNode, CurrentNode.neighbors[i], distanceType)

#                     if CurrentNode.neighbors[i] in OpenSet:
#                         # if neighbors is in OpenSet, we already visited the neighbor and it already has a g value, so check if this is a shorter path
#                         # then I have found a shorter path, update g value and redirect to new parent.... f & h value will be updated below if statement
#                         if tempG < CurrentNode.neighbors[i].g:
#                             CurrentNode.neighbors[i].g = tempG
#                             CurrentNode.neighbors[i].Parent = CurrentNode
#                     else:
#                         # Step 2e-3: if neigbor not in open : add neigbor to open
#                         # this is a new node to explore and we set the g value to this node
#                         CurrentNode.neighbors[i].g = tempG
#                         OpenSet.append(CurrentNode.neighbors[i])
#                         CurrentNode.neighbors[i].Parent = CurrentNode

#                     # Step 2e-2: set f cost of neigbor
#                     CurrentNode.neighbors[i].h = heuristic(
#                         CurrentNode.neighbors[i], EndNode)
#                     CurrentNode.neighbors[i].f = CurrentNode.neighbors[i].g + \
#                         CurrentNode.neighbors[i].h

#         # Draw grid
#         if DrawGrid:
#             updateGrid(OpenSet, ClosedSet, grid, win)

#         iLoop += 1
#     return OpenSet, ClosedSet, StartNode, EndNode


# if __name__ == "__main__":
#     Test_A_Star()
