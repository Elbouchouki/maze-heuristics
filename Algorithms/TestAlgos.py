from Maze import init_test, init_grid
from Params import *
from Graphics import *
from Utils import draw_path, updateGrid
from .Astar import astar
from .Dijkstra import dijkstra


def prepareTest(TestName: str, grid):
    grid, OpenSet, ClosedSet, StartNode, EndNode = init_test(grid=grid)
    win = None
    if DrawGrid:
        win = GraphWin(TestName,
                       height, width, autoflush=False)
        updateGrid(OpenSet=OpenSet, ClosedSet=ClosedSet, grid=grid, win=win)
        if (waitForStart):
            input("wait for start")

    return grid, OpenSet, ClosedSet, StartNode, EndNode, win


def Test_A_Star(grid, distanceType="euclidienne"):
    testname = "Astar "+distanceType.capitalize()
    grid, OpenSet, ClosedSet, StartNode, EndNode, win = prepareTest(
        TestName=testname, grid=grid)

    OpenSet, ClosedSet, StartNode, EndNode, execution = astar(
        distanceType=distanceType, OpenSet=OpenSet, ClosedSet=ClosedSet, StartNode=StartNode, EndNode=EndNode, grid=grid, win=win)

    solutionLength = draw_path(StartNode, EndNode, win)

    if (waitForStart):
        input("")
    if DrawGrid:
        win.close()
    return {
        "testname": testname,
        "pathLength": solutionLength,
        "opened": len(OpenSet),
        "explored": len(ClosedSet),
        "execution": execution
    }


def Test_Dijkstra(grid=init_grid()):
    testname = "Dijkstra"
    grid, OpenSet, ClosedSet, StartNode, EndNode, win = prepareTest(
        testname, grid)

    # here astar algorithm
    OpenSet, ClosedSet, StartNode, EndNode, execution = dijkstra(
        OpenSet=OpenSet, ClosedSet=ClosedSet, StartNode=StartNode, EndNode=EndNode, grid=grid, win=win)
    # here solution drawing if exists
    solutionLength = draw_path(StartNode, EndNode, win)

    if (waitForStart):
        input("")
    if DrawGrid:
        win.close()

    return {
        "testname": testname,
        "pathLength": solutionLength,
        "opened": len(OpenSet),
        "explored": len(ClosedSet),
        "execution": execution
    }
