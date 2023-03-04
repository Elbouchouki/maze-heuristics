from Maze import init_test, init_grid
from Params import *
from Graphics import *
from .utils import draw_path, updateGrid
from .Astar import astar
from .Dijkstra import dijkstra


def A_Start_Distants_Tests():
    grid = init_grid()
    Test_A_Star(grid=grid, distanceType="euclidienne")
    Test_A_Star(grid=grid, distanceType="manhattan")


def Test_A_Star(grid=init_grid(), distanceType="euclidienne", waitForStart=True):
    # Initialisation of grid
    grid, OpenSet, ClosedSet, StartNode, EndNode = init_test(grid)
    # check if ui is enabled
    if DrawGrid:
        win = GraphWin(distanceType.capitalize(),
                       height, width, autoflush=False)
        updateGrid(OpenSet=OpenSet, ClosedSet=ClosedSet, grid=grid, win=win)
        if (waitForStart):
            input("wait for start")

    # here astar algorithm
    OpenSet, ClosedSet, StartNode, EndNode = astar(
        distanceType=distanceType, OpenSet=OpenSet, ClosedSet=ClosedSet, StartNode=StartNode, EndNode=EndNode, grid=grid, win=win)
    # here solution drawing if exists
    solutionLength = draw_path(StartNode, EndNode, win)

    print("solutionLength : ", solutionLength)
    print("OpenSet : ", len(OpenSet))
    print("ClosedSet : ", len(ClosedSet))

    input("")
    if DrawGrid:
        win.close()
    return solutionLength, len(OpenSet), len(ClosedSet)


def Test_Dijkstra(waitForStart=True):
    # Initialisation of grid
    grid, OpenSet, ClosedSet, StartNode, EndNode = init_test()
    # check if ui is enabled
    if DrawGrid:
        win = GraphWin("Dijkstra",
                       height, width, autoflush=False)
        updateGrid(OpenSet=OpenSet, ClosedSet=ClosedSet, grid=grid, win=win)
        if (waitForStart):
            input("wait for start")

    # here astar algorithm
    OpenSet, ClosedSet, StartNode, EndNode = dijkstra(
        OpenSet=OpenSet, ClosedSet=ClosedSet, StartNode=StartNode, EndNode=EndNode, grid=grid, win=win)
    # here solution drawing if exists
    solutionLength = draw_path(StartNode, EndNode, win)

    print("solutionLength : ", solutionLength)
    print("OpenSet : ", len(OpenSet))
    print("ClosedSet : ", len(ClosedSet))

    input("")
    if DrawGrid:
        win.close()
    return solutionLength, len(OpenSet), len(ClosedSet)
