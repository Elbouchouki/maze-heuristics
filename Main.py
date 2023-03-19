from Algorithms import Test_A_Star, Test_Dijkstra, Test_DepthFirstSearch, Test_BestFirstSearch, Test_BreadthFirstSearch, printSolution
from Maze import imageToGrid, init_grid
from Params import *
import math
import sys
import getopt
from pympler import asizeof


def ay(sol):
    return str(sol["pathLength"])+" | "+str(sol["explored"])+" ("+str(round(sol["execution"], 2))+(" s)" if TIME_V == 1 else " ms)")


def runAll(s, algo):
    grid = imageToGrid("./exemples/"+s+".png")

    temp1 = algo(grid=grid, distanceType="euclidienne")
    temp2 = algo(grid=grid, distanceType="manhattan")
    temp3 = algo(grid=grid, distanceType="tchebychev")
    temp4 = algo(grid=grid, distanceType="minkowski")
    temp5 = Test_Dijkstra(grid=grid)

    return [ay(temp1), ay(temp2), ay(temp3), ay(temp4), ay(temp5)]


def compareAll(algo):
    graphs = [
        # "small",
        # "normal",
        # "large",
        "25x25", "40x40", "50x50",
        "60x60-b",
        # "100x100-best"
    ]
    d = {"Maze": ["Euclidianne", "Mnhathan",
                  "Tchebychev", "Minkowski", "Dijkstra"]}
    for s in graphs:
        d[s] = runAll(s, algo)
    for k, v in d.items():
        if (k.endswith('b')):
            print("")

        euclidienne, manhattan, tchebychev, minkowski, dijkstra = v
        print("{:<10} {:<25} {:<25} {:<25} {:<25} {:<25}".format(
            k, euclidienne, manhattan, tchebychev, minkowski, dijkstra))


def compare():
    print("-> BestFirstSearch")
    compareAll(Test_BestFirstSearch)
    print("-> A*")
    compareAll(Test_A_Star)


def getMazeSize(maze):
    spot_size = asizeof.asizeof(maze[0][0])*1e-6
    print(spot_size*2000*2000)


def optParse(opts):
    gridType = None
    comparaison = None
    algorithm = None
    distance = None
    toBeCompared = None
    for opt, arg in opts:
        if opt == '-g':
            gridType = arg
        if opt == '-c':
            comparaison = arg
        if opt == '-a':
            algorithm = arg
        if opt == '-d':
            distance = arg
        if opt == '-t':
            toBeCompared = arg
    return gridType, comparaison, algorithm, distance, toBeCompared


def gridFactory(gridType):
    grid = None
    if gridType == "autogenerate":
        grid = init_grid()
    else:
        grid = imageToGrid(gridType)
    return grid


def algorithmFactory(algorithm="astar"):
    if algorithm == "astar":
        return Test_A_Star
    if algorithm == "dijkstra":
        return Test_Dijkstra
    if algorithm == "breadthFirstSearch":
        return Test_BreadthFirstSearch
    if algorithm == "depthFirstSearch":
        return Test_DepthFirstSearch
    if algorithm == "bestFirstSearch":
        return Test_BestFirstSearch


def toBeComparedFactory(toBeCompared):
    if toBeCompared == "astar":
        return Test_A_Star
    if toBeCompared == "bestFirstSearch":
        return Test_BestFirstSearch


if __name__ == "__main__":
    opts, args = getopt.getopt(sys.argv[1:], "g:c:t:a:d:", [
                               'gridType', 'comparaison', 'toBeCompared', 'algorithmType', 'distanceType'])

    gridType, comparaison, algorithmType, distanceType, toBeCompared = optParse(
        opts)
    grid = gridFactory(gridType)

    if (comparaison):
        if (toBeCompared):
            compareAll(toBeComparedFactory(toBeCompared))
        else:
            compare()
        exit(0)

    algorithm = algorithmFactory(algorithmType)
    try:
        print(printSolution(algorithm(grid, distanceType)))
    except:
        print("No Path Found")
