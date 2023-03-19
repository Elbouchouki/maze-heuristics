from MazeVersion2 import MazeV2
# from collections import deque
# stack = deque([start])


def bredthFirstSearch(maze_graph: MazeV2):

    openSet = []
    closedSet = []

    StartNode = maze_graph.start
    EndNode = maze_graph.end

    openSet.append(StartNode)

    isFound = False

    while (openSet):

        CurrentNode = openSet.pop()
        closedSet.append(CurrentNode)

        if (CurrentNode == EndNode):
            isFound = True
            break

        # for i in range(0, 4):
        #     if (CurrentNode.Neighbours[i] not in closedSet):
        #         CurrentNode.Neighbours[i].Parent = CurrentNode
        #         if (CurrentNode.Neighbours[i] not in openSet):
        #             openSet.append(CurrentNode.Neighbours[i])
        for neighbor in CurrentNode.Neighbours:
            if (neighbor is not None and neighbor not in closedSet):
                if (neighbor not in openSet):
                    neighbor.Parent = CurrentNode
                    openSet.append(neighbor)

    return openSet, closedSet, StartNode, EndNode, isFound
