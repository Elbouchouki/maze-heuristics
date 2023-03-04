from Graphics import *
from Params import *


def updateGrid(OpenSet, ClosedSet, grid, win):
    for j in range(len(grid[0])):
        for i in range(len(grid)):

            if grid[i][j].isWall:
                grid[i][j].show(win, NODE_BORDER)
            else:
                grid[i][j].show(win, NODE_EMPTY)

    for j in range(len(OpenSet)):
        OpenSet[j].show(win, NODE_OPENED)

    for j in range(len(ClosedSet)):
        ClosedSet[j].show(win, NODE_CLOSED)

    update(changeRate)


def draw_path(StartNode, EndNode, win):
    if DrawGrid:
        StartNode.show(win, NODE_PATH)
        EndNode.show(win, NODE_PATH)
        update(PathchangeRate)

    previous = EndNode.Parent
    ContinueSearch = True
    solutionLength = 2

    while ContinueSearch:
        solutionLength = solutionLength+1
        if DrawGrid:
            previous.show(win, NODE_PATH)
            update(PathchangeRate)
        previous = previous.Parent
        if previous == StartNode:
            ContinueSearch = False

    return solutionLength
