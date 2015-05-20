import sys, pygame, math, numpy, random, time, copy, ipdb
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
    y           = 0
    x           = 0
    i           = 0
    j           = 0
    points      = world.getPoints()

    def isValidCell(cellBounds):
        for point in points:
            xLowerBound = cellBounds[0]
            yLowerBound = cellBounds[1]
            xUpperBound = cellBounds[0] + cellsize
            yUpperBound = cellBounds[1] + cellsize

            if point[0] < xUpperBound and point[0] > xLowerBound and point[1] < yUpperBound and point[1] > yLowerBound:
                return False
        return True


    ### YOUR CODE GOES BELOW HERE ###
    # Calculate row and column numbers
    while y < SCREEN[1]:
        num_rows    += 1
        y           += cellsize
        while x < SCREEN[0]:
            num_columns += 1
            x           += cellsize

    dimensions  = (num_columns, num_rows)
    grid        = [[10 for i in range(num_rows+1)] for j in range(num_columns+1)]

    # Calculate bounds of each cell and create grid
    for y in range(0, SCREEN[1], int(38)):
        j  = 0
        i  = 0
        for x in range(0, SCREEN[0], int(38)):
            j += 1
            i += 1
            cellBounds = (x,y)
            grid[j][i] = isValidCell(cellBounds)

    ### YOUR CODE GOES ABOVE HERE ###
    return grid, dimensions

