import sys


height = 800
width = 800
cols = 30
rows = 30
w = height/rows
h = width/cols
WallPercentage = 30
DrawGrid = bool(sys.argv[-1] == "True")
waitForStart = bool(sys.argv[-1] == "True")

NODE_EMPTY = 'white'
NODE_BORDER = 'black'
NODE_PATH = 'green'
NODE_OPENED = 'yellow'
NODE_CLOSED = 'red'


TIME_V = 1000

changeRate = 10
PathchangeRate = 10000000


minkowski_p = 100
