from Maze import init_test, init_grid
from Params import *
from Graphics import *
from Utils import draw_path, updateGrid
from .Astar import astar
from .Dijkstra import dijkstra
from .depthFirstSearch import depthFirstSearch
from .breadthFirstSearch import breadthFirstSearch
from .bestFirstSearch import bestFirstSearch


def printSolution(solution):
    print("Algorithm -> ", solution["testname"])
    print("SolutionLength : ", solution["pathLength"])
    print("In queue : ", solution["opened"])
    print("Explored : ", solution["explored"])
    print("Execution time : ", solution["execution"])


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


def Test_A_Star(grid, distanceType):
    testname = "Astar "+distanceType.capitalize()
    return Test(testname, grid, lambda OpenSet, ClosedSet, StartNode, EndNode, grid, win: astar(distanceType=distanceType, OpenSet=OpenSet, ClosedSet=ClosedSet, StartNode=StartNode, EndNode=EndNode, grid=grid, win=win))


def Test_BestFirstSearch(grid, distanceType):
    testname = "BestFirstSearch "+distanceType.capitalize()
    return Test(testname, grid, lambda OpenSet, ClosedSet, StartNode, EndNode, grid, win: bestFirstSearch(distanceType=distanceType, OpenSet=OpenSet, ClosedSet=ClosedSet, StartNode=StartNode, EndNode=EndNode, grid=grid, win=win))


def Test_Dijkstra(grid):
    return Test("Dijkstra", grid, dijkstra)


def Test_DepthFirstSearch(grid):
    return Test("DepthFirstSearch", grid, depthFirstSearch)


def Test_BreadthFirstSearch(grid):
    return Test("BreadthFirstSearch", grid, breadthFirstSearch)


def Test(TestName: str, grid, algorithm):
    testname = TestName
    grid, OpenSet, ClosedSet, StartNode, EndNode, win = prepareTest(
        testname, grid)

    # here astar algorithm
    OpenSet, ClosedSet, StartNode, EndNode, execution = algorithm(
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
