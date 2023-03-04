from Graphics import *
from Params import *


def updateGrid(OpenSet, ClosedSet, grid, win):
    for j in range(cols):
        for i in range(rows):

            if grid[i][j].isWall:
                grid[i][j].show(win, 'black')
            else:
                grid[i][j].show(win, 'blue')

    for j in range(len(OpenSet)):
        OpenSet[j].show(win, 'green')

    for j in range(len(ClosedSet)):
        ClosedSet[j].show(win, 'red')

    update(changeRate)


def draw_path(StartNode, EndNode, win):
    if DrawGrid:
        StartNode.show(win, 'yellow')
        EndNode.show(win, 'yellow')
        update(changeRate)

    previous = EndNode.Parent
    ContinueSearch = True
    solutionLength = 2

    while ContinueSearch:
        solutionLength = solutionLength+1
        if DrawGrid:
            previous.show(win, 'yellow')
            update(changeRate)
        previous = previous.Parent
        if previous == StartNode:
            ContinueSearch = False

    return solutionLength
