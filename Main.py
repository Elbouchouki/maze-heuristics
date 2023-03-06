from Algorithms import Test_A_Star, Test_Dijkstra, Test_DepthFirstSearch, Test_BestFirstSearch, Test_BreadthFirstSearch, printSolution
from Maze import imageToGrid, init_grid
from Params import *
import math

# euclidienne
# manhattan
# tchebychev
# minkowski


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
        # "60x60-b",
        # "100x100-best"
    ]
    d = {"Maze": ["Euclidianne", "Mnhathan",
                  "Tchebychev", "Minkowski", "Dijkstra"]}
    for s in graphs:
        d[s] = runAll(s, algo)
    for k, v in d.items():
        euclidienne, manhattan, tchebychev, minkowski, dijkstra = v
        print("{:<10} {:<25} {:<25} {:<25} {:<25} {:<25}".format(
            k, euclidienne, manhattan, tchebychev, minkowski, dijkstra))
    # print(d)


def compare():
    print("-> BestFirstSearch")
    compareAll(Test_BestFirstSearch)
    print("-> A*")
    compareAll(Test_A_Star)


def tests(grid):

    # printSolution(Test_BreadthFirstSearch(grid=grid))

    # print()

    # printSolution(Test_DepthFirstSearch(grid=grid))

    # print()

    printSolution(Test_BestFirstSearch(grid=grid, distanceType="manhattan"))

    # print()

    # printSolution(Test_A_Star(grid=grid, distanceType="euclidienne"))

    # print()

    # printSolution(Test_A_Star(grid=grid, distanceType="manhattan"))

    # print()

    # printSolution(Test_A_Star(grid=grid, distanceType="tchebychev"))

    # print()

    # printSolution(Test_A_Star(grid=grid, distanceType="minkowski"))

    # print()

    # printSolution(Test_Dijkstra(grid=grid))


if __name__ == "__main__":
    # grid = imageToGrid('./exemples/25x25.png')
    # grid = init_grid()
    # tests(grid)
    # compareAll(Test_A_Star)
    compare()
