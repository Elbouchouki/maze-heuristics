from PIL import Image
import time
from MazeVersion2 import MazeV2
Image.MAX_IMAGE_PIXELS = None


def solve(input_file):
    print("Loading Image")
    im = Image.open(input_file)

    print("Creating Maze")
    t0 = time.time()
    maze = MazeV2(im)
    t1 = time.time()
    print("Node Count:", maze.count)
    total = t1-t0
    print("Time elapsed:", total, "\n")


def ImageToMazeGraphVersion(img):
    im = Image.open(img)
    t0 = time.time()
    maze = MazeV2(im)
    t1 = time.time()
    total = t1-t0
    return maze, total


def SaveResult(im, output_file):
    print("Saving Image")
    im = im.convert('RGB')
    impixels = im.load()

    resultpath = [n.Position for n in result]

    length = len(resultpath)

    for i in range(0, length - 1):
        a = resultpath[i]
        b = resultpath[i+1]

        # Blue - red
        r = int((i / length) * 255)
        px = (r, 0, 255 - r)

        if a[0] == b[0]:
            # Ys equal - horizontal line
            for x in range(min(a[1], b[1]), max(a[1], b[1])):
                impixels[x, a[0]] = px
        elif a[1] == b[1]:
            # Xs equal - vertical line
            for y in range(min(a[0], b[0]), max(a[0], b[0]) + 1):
                impixels[a[1], y] = px

    im.save(output_file)
