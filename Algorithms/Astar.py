from .Distances import heuristic
from .utils import updateGrid
from Params import *


def get_best_heuristic(OpenSet):
    winner_index = 0
    for i in range(len(OpenSet)):
        if OpenSet[i].f < OpenSet[winner_index].f:
            winner_index = i
    return OpenSet[winner_index]


def astar(OpenSet, ClosedSet, StartNode, EndNode, grid, win, distanceType="euclidienne"):
    StartNode.g = 0
    StartNode.h = heuristic(StartNode, EndNode, distanceType)
    StartNode.f = StartNode.h + StartNode.g
    OpenSet.append(StartNode)
    ContinueSearch = True
    iLoop = 1
    # Step1 -  Start the loop to find the best solution
    while ContinueSearch:

        CurrentNode = get_best_heuristic(OpenSet)

        # Step 2b remove current node from open list
        OpenSet.remove(CurrentNode)

        # Step 2c add current node to closed list
        ClosedSet.append(CurrentNode)

        # Step 2d if current node is target node we found optimal path and exit loop
        if CurrentNode == EndNode:
            ContinueSearch = False

        # Step 2e for each neighbor in the current node
        for i in range(len(CurrentNode.neighbors)):

            # Step 2e-1 if:neigbor is not traversable or neighbor in closed goto next neighbor
            if (CurrentNode.neighbors[i] not in ClosedSet) and (CurrentNode.neighbors[i].isWall == False):
                # set tentative gscore to gscore(current)+dist(current,neightbor)

                # Step 2e-2 else: if (new_path to neighbor is shorter) or (neigbor is not in openlist)

                if (CurrentNode.neighbors[i] not in ClosedSet):
                    # use heuristic function for determing stepsize
                    tempG = CurrentNode.g + \
                        heuristic(
                            CurrentNode, CurrentNode.neighbors[i], distanceType)

                    if CurrentNode.neighbors[i] in OpenSet:
                        # if neighbors is in OpenSet, we already visited the neighbor and it already has a g value, so check if this is a shorter path
                        # then I have found a shorter path, update g value and redirect to new parent.... f & h value will be updated below if statement
                        if tempG < CurrentNode.neighbors[i].g:
                            CurrentNode.neighbors[i].g = tempG
                            CurrentNode.neighbors[i].Parent = CurrentNode
                    else:
                        # Step 2e-3: if neigbor not in open : add neigbor to open
                        # this is a new node to explore and we set the g value to this node
                        CurrentNode.neighbors[i].g = tempG
                        OpenSet.append(CurrentNode.neighbors[i])
                        CurrentNode.neighbors[i].Parent = CurrentNode

                    # Step 2e-2: set f cost of neigbor
                    CurrentNode.neighbors[i].h = heuristic(
                        CurrentNode.neighbors[i], EndNode)
                    CurrentNode.neighbors[i].f = CurrentNode.neighbors[i].g + \
                        CurrentNode.neighbors[i].h

        # Draw grid
        if DrawGrid:
            updateGrid(OpenSet=OpenSet, ClosedSet=ClosedSet,
                       grid=grid, win=win)

        iLoop += 1
    return OpenSet, ClosedSet, StartNode, EndNode
