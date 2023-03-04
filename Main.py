from Algorithms import Test_A_Star, Test_Dijkstra
from Maze import imageToGrid, init_grid
from Params import *
# euclidienne
# manhattan
# tchebychev
# minkowski


def printSolution(solution):
    print("Algorithm -> ", solution["testname"])
    print("SolutionLength : ", solution["pathLength"])
    print("In queue : ", solution["opened"])
    print("Explored : ", solution["explored"])
    print("Execution time : ", solution["execution"])


if __name__ == "__main__":
    grid = imageToGrid('./exemples/100x100.png')
    # grid = init_grid()

    # printSolution(Test_A_Star(grid=grid, distanceType="euclidienne"))

    # print()

    # printSolution(Test_A_Star(grid=grid, distanceType="manhattan"))

    # print()

    printSolution(Test_A_Star(grid=grid, distanceType="tchebychev"))

    print()

    printSolution(Test_A_Star(grid=grid, distanceType="minkowski"))
    # print()

    # printSolution(Test_Dijkstra(grid=grid))
