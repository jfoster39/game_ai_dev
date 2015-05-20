import sys, pygame, math, numpy, random, time, copy
from pygame.locals import *

from constants import *
from utils import *
from core import *

# Creates a grid as a 2D array of True/False values (True =  traversable). Also returns the dimensions of the grid as a (columns, rows) list.
def myCreateGrid(world, cellsize):
    grid        = None
    dimensions  = (0, 0)
    num_columns = 0
    num_rows    = 0
    y           = cellsize
    x           = cellsize
    ### YOUR CODE GOES BELOW HERE ###
    while y < SCREEN[1]:
        num_rows    += 1
        y           += cellsize
        while x < SCREEN[0]:
            num_columns += 1
            x           += cellsize

    dimensions  = (num_columns, num_rows)
    grid        = [[True for i in range(num_rows)] for j in range(num_columns)]

    ### YOUR CODE GOES ABOVE HERE ###
    return grid, dimensions

