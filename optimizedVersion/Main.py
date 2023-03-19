from Solver import ImageToMazeGraphVersion
from algorithms import bredthFirstSearch, extract_path

from pympler import asizeof

from collections import deque


def solve(maze):
    start = maze.start
    end = maze.end

    width = maze.width

    queue = deque([start])
    shape = (maze.height, maze.width)
    prev = [None] * (maze.width * maze.height)
    visited = [False] * (maze.width * maze.height)

    count = 0

    completed = False

    visited[start.Position[0] * width + start.Position[1]] = True

    while queue:
        count += 1
        current = queue.pop()

        if current == end:
            completed = True
            break

        for n in current.Neighbours:
            if n != None:
                npos = n.Position[0] * width + n.Position[1]
                if visited[npos] == False:
                    queue.appendleft(n)
                    visited[npos] = True
                    prev[npos] = current

    path = deque()
    current = end
    while (current != None):
        path.appendleft(current)
        current = prev[current.Position[0] * width + current.Position[1]]

    return path, count, completed


def main():
    maze, total = ImageToMazeGraphVersion("exemples/small.png")
    openSet, closedSet, start, end, isFound = bredthFirstSearch(maze)
    print(len(openSet), len(closedSet), isFound)
    print(len(extract_path(end)))
    path, count, completed = solve(maze)
    print(len(path))
    # print(total)
    # size = asizeof.asizeof(maze)
    # print("total: ", total)
    # print("size: ", size)


if __name__ == "__main__":
    main()
