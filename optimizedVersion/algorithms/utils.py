import time
from MazeVersion2 import MazeV2
from collections import deque


def calculate_time(algorithms):
    t0 = time.time()

    result = algorithms()

    t1 = time.time()
    return {"result": result, "time": t1-t0}


def extract_path(end: MazeV2.Node):
    path = deque()
    current: MazeV2.Node = end
    while (current is not None):
        path.appendleft(current)
        current = current.Parent
    return path
