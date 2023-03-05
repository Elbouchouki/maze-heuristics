from Algorithms import Test_A_Star, A_Start_Distants_Tests, Test_Dijkstra
from Maze import imageToGrid, init_grid
from Params import *
# euclidienne
# manhattan
# tchebychev


def printSolution(solution):
    print("Algorithm -> ", solution["testname"])
    print("SolutionLength : ", solution["pathLength"])
    print("In queue : ", solution["opened"])
    print("Explored : ", solution["explored"])
    if (waitForStart):
        input("")

# // axawa had l3jeb 
if __name__ == "__main__":
    # A_Start_Distants_Tests()
    # grid = imageToGrid('./exemples/normal.png')
    grid = init_grid()
    printSolution(Test_A_Star(grid=grid, distanceType="euclidienne"))
    print()
    printSolution(Test_A_Star(grid=grid, distanceType="manhattan"))
    print()
    printSolution(Test_A_Star(grid=grid, distanceType="tchebychev"))
    print()
    printSolution(Test_Dijkstra(grid=grid))
