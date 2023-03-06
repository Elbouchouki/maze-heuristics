from .Distances import heuristic
from Utils import updateGrid
from Params import *
import time


def get_best(OpenSet, EndNode, distanceType):
    winner_index = 0
    winner_heuristic = heuristic(OpenSet[winner_index], EndNode, distanceType)
    for i in range(len(OpenSet)):
        current_heuristic = heuristic(OpenSet[i], EndNode, distanceType)
        if current_heuristic < winner_heuristic:
            winner_index = i
            winner_heuristic = current_heuristic
    return OpenSet[winner_index]


def bestFirstSearch(OpenSet, ClosedSet, StartNode, EndNode, grid, win, distanceType="euclidienne"):
    start = time.time()
    lisr = []
    OpenSet.append(StartNode)
    ContinueSearch = True
    while ContinueSearch:

        CurrentNode = get_best(OpenSet, EndNode, distanceType)

        OpenSet.remove(CurrentNode)

        ClosedSet.append(CurrentNode)

        if CurrentNode == EndNode:
            ContinueSearch = False

        for i in range(len(CurrentNode.neighbors)):
            if (CurrentNode.neighbors[i] not in ClosedSet) and (CurrentNode.neighbors[i].isWall == False):
                CurrentNode.neighbors[i].Parent = CurrentNode
                if CurrentNode.neighbors[i] not in OpenSet:
                    OpenSet.append(CurrentNode.neighbors[i])

        if DrawGrid:
            updateGrid(OpenSet=OpenSet, ClosedSet=ClosedSet,
                       grid=grid, win=win)
    end = time.time()
    execution = (end-start) * TIME_V

    return OpenSet, ClosedSet, StartNode, EndNode, execution
