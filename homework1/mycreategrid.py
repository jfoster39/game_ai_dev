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
    y           = 0
    x           = 0
    i           = 0
    j           = 0
    lines       = world.getLinesWithoutBorders()
    obstacles   = world.getObstacles()

    def isValidCell(cellBounds):
        xLowerBound = cellBounds[0]
        yLowerBound = cellBounds[1]
        xUpperBound = cellBounds[0] + cellsize
        yUpperBound = cellBounds[1] + cellsize

        cellPointTopLeft    = (xLowerBound, yLowerBound)
        cellPointBottomLeft = (xLowerBound, yUpperBound)
        cellPointTopRight   = (xUpperBound, yLowerBound)
        cellPointBottomRight= (xUpperBound, yUpperBound)

        for obstacle in obstacles:
            if obstacle.pointInside(cellPointTopLeft):
                return False

        for line in lines:
            if ( calculateIntersectPoint( cellPointTopLeft, cellPointTopRight, line[0], line[1] ) or
                    calculateIntersectPoint( cellPointTopLeft, cellPointBottomLeft, line[0], line[1] ) or
                    calculateIntersectPoint( cellPointBottomLeft, cellPointBottomRight, line[0], line[1] ) or
                    calculateIntersectPoint( cellPointTopRight, cellPointBottomRight, line[0], line[1] ) ):
                return False

        return True

    # Calculate row and column numbers
    while y < SCREEN[1]:
        num_rows    += 1
        y           += cellsize
        while x < SCREEN[0]:
            num_columns += 1
            x           += cellsize

    dimensions  = (num_columns-1, num_rows-1)
    grid        = [[0 for i in range(num_rows)] for j in range(num_columns)]

    # Calculate bounds of each cell and create grid
    j = -1
    for y in range(0, SCREEN[1], int(38)):
        j += 1
        i  = 0
        for x in range(0, SCREEN[0], int(38)):
            cellBounds = (x,y)
            grid[i][j] = isValidCell(cellBounds)
            i += 1

    return grid, dimensions
