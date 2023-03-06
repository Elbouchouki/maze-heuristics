from Utils import updateGrid
from Params import *
import time


def get_minimum(OpenSet):
    winner_index = 0
    for i in range(len(OpenSet)):
        if OpenSet[i].g < OpenSet[winner_index].g:
            winner_index = i
    return OpenSet[winner_index]


def dijkstra(OpenSet, ClosedSet, StartNode, EndNode, grid, win):
    start = time.time()
    StartNode.g = 0
    OpenSet.append(StartNode)
    ContinueSearch = True
    while ContinueSearch:

        CurrentNode = get_minimum(OpenSet)

        OpenSet.remove(CurrentNode)

        ClosedSet.append(CurrentNode)

        if CurrentNode == EndNode:
            ContinueSearch = False

        for i in range(len(CurrentNode.neighbors)):
            if (CurrentNode.neighbors[i] not in ClosedSet) and (CurrentNode.neighbors[i].isWall == False):
                if CurrentNode.neighbors[i] in OpenSet:
                    if CurrentNode.g < CurrentNode.neighbors[i].g:
                        CurrentNode.neighbors[i].g = CurrentNode.g + 1
                        CurrentNode.neighbors[i].Parent = CurrentNode
                else:
                    CurrentNode.neighbors[i].g = CurrentNode.g + 1
                    OpenSet.append(CurrentNode.neighbors[i])
                    CurrentNode.neighbors[i].Parent = CurrentNode

        if DrawGrid:
            updateGrid(OpenSet=OpenSet, ClosedSet=ClosedSet,
                       grid=grid, win=win)
    end = time.time()
    execution = (end-start) * TIME_V

    return OpenSet, ClosedSet, StartNode, EndNode, execution
