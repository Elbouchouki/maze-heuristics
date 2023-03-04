from Maze import init_test, init_grid
from Params import *
from Graphics import *
from Utils import draw_path, updateGrid
from .Astar import astar
from .Dijkstra import dijkstra


# testName: str,


def prepareTest(TestName: str, grid=init_grid()):
    grid, OpenSet, ClosedSet, StartNode, EndNode = init_test(grid)
    win = None
    if DrawGrid:
        win = GraphWin(TestName,
                       height, width, autoflush=False)
        updateGrid(OpenSet=OpenSet, ClosedSet=ClosedSet, grid=grid, win=win)
        if (waitForStart):
            input("wait for start")

    return grid, OpenSet, ClosedSet, StartNode, EndNode, win


def printSolution(TestName: str, solutionLength, OpenSet, ClosedSet):
    print("solutionLength : ", solutionLength)
    print("OpenSet : ", OpenSet)
    print("ClosedSet : ", ClosedSet)
    if (waitForStart):
        input("")


def A_Start_Distants_Tests():
    grid = init_grid()
    Test_A_Star(grid=grid, distanceType="euclidienne")
    Test_A_Star(grid=grid, distanceType="manhattan")


def Test_A_Star(grid=init_grid(), distanceType="euclidienne") -> {str, int, int, int}:
    testname = "Astar "+distanceType.capitalize()
    grid, OpenSet, ClosedSet, StartNode, EndNode, win = prepareTest(
        testname, grid)

    OpenSet, ClosedSet, StartNode, EndNode = astar(
        distanceType=distanceType, OpenSet=OpenSet, ClosedSet=ClosedSet, StartNode=StartNode, EndNode=EndNode, grid=grid, win=win)

    solutionLength = draw_path(StartNode, EndNode, win)

    if DrawGrid:
        win.close()
    return {
        "testname": testname,
        "pathLength": solutionLength,
        "opened": len(OpenSet),
        "explored": len(ClosedSet)
    }


def Test_Dijkstra(grid=init_grid()):
    # Initialisation of grid
    # grid, OpenSet, ClosedSet, StartNode, EndNode = init_test(grid)
    # # check if ui is enabled
    # win = None
    # if DrawGrid:
    #     win = GraphWin("Dijkstra",
    #                    height, width, autoflush=False)
    #     updateGrid(OpenSet=OpenSet, ClosedSet=ClosedSet, grid=grid, win=win)
    #     if (waitForStart):
    #         input("wait for start")

    testname = "Dijkstra"
    grid, OpenSet, ClosedSet, StartNode, EndNode, win = prepareTest(
        testname, grid)

    # here astar algorithm
    OpenSet, ClosedSet, StartNode, EndNode = dijkstra(
        OpenSet=OpenSet, ClosedSet=ClosedSet, StartNode=StartNode, EndNode=EndNode, grid=grid, win=win)
    # here solution drawing if exists
    solutionLength = draw_path(StartNode, EndNode, win)

    if DrawGrid:
        win.close()

    return {
        "testname": testname,
        "pathLength": solutionLength,
        "opened": len(OpenSet),
        "explored": len(ClosedSet)
    }
