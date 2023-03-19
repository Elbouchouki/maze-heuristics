from Utils import updateGrid
from Params import *
import time


def breadthFirstSearch(OpenSet, ClosedSet, StartNode, EndNode, grid, win):
    start = time.time()
    OpenSet.append(StartNode)
    ContinueSearch = True
    while ContinueSearch:

        CurrentNode = OpenSet.pop(0)
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
