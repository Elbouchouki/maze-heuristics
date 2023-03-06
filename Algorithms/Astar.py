from .Distances import heuristic
from Utils import updateGrid
from Params import *
import time


def get_best_heuristic(OpenSet):
    winner_index = 0
    for i in range(len(OpenSet)):
        if OpenSet[i].f < OpenSet[winner_index].f:
            winner_index = i
    return OpenSet[winner_index]


def astar(OpenSet, ClosedSet, StartNode, EndNode, grid, win, distanceType="euclidienne"):
    start = time.time()
    StartNode.g = 0
    StartNode.h = heuristic(StartNode, EndNode, distanceType)
    StartNode.f = StartNode.h + StartNode.g
    OpenSet.append(StartNode)
    ContinueSearch = True

    while ContinueSearch:

        CurrentNode = get_best_heuristic(OpenSet)

        OpenSet.remove(CurrentNode)

        ClosedSet.append(CurrentNode)

        if CurrentNode == EndNode:
            ContinueSearch = False

        for i in range(len(CurrentNode.neighbors)):

            if (CurrentNode.neighbors[i] not in ClosedSet) and (CurrentNode.neighbors[i].isWall == False):

                if (CurrentNode.neighbors[i] not in ClosedSet):
                    tempG = CurrentNode.g + 1
                    # \
                    #     heuristic(
                    #         CurrentNode, CurrentNode.neighbors[i], distanceType)

                    if CurrentNode.neighbors[i] in OpenSet:
                        if tempG < CurrentNode.neighbors[i].g:
                            CurrentNode.neighbors[i].g = tempG
                            CurrentNode.neighbors[i].Parent = CurrentNode
                    else:
                        CurrentNode.neighbors[i].g = tempG
                        OpenSet.append(CurrentNode.neighbors[i])
                        CurrentNode.neighbors[i].Parent = CurrentNode

                    CurrentNode.neighbors[i].h = heuristic(
                        CurrentNode.neighbors[i], EndNode, distanceType)
                    CurrentNode.neighbors[i].f = CurrentNode.neighbors[i].g + \
                        CurrentNode.neighbors[i].h

        if DrawGrid:
            updateGrid(OpenSet=OpenSet, ClosedSet=ClosedSet,
                       grid=grid, win=win)

    end = time.time()
    execution = (end-start) * TIME_V

    return OpenSet, ClosedSet, StartNode, EndNode, execution
