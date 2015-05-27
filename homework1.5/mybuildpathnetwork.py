import sys, pygame, math, numpy, random, time, copy, operator
from pygame.locals import *

from constants import *
from utils import *
from core import *

# Creates the pathnetwork as a list of lines between all pathnodes that are traversable by the agent.
def myBuildPathNetwork(pathnodes, world, agent = None):
    lines                   = []
    pathNodesCopy           = copy.copy( pathnodes )
    obstacleLines           = world.getLinesWithoutBorders()
    obstaclePoints          = world.getPoints()
    minCollisionDistance    = agent.radius * 2
    ### YOUR CODE GOES BELOW HERE ###

    # Find all lines between pathnodes which do not intersect obstacle.
    for pathNode in pathnodes:
        for pathNodeCopy in pathNodesCopy:
            if ( cmp( pathNode, pathNodeCopy ) != 0 and
                    rayTraceWorld( pathNode, pathNodeCopy, obstacleLines ) == None ):

                # Calculate distance from nearest obstacle point to line.
                distance = INFINITY
                for point in obstaclePoints:
                    minDistance = minimumDistance( (pathNode, pathNodeCopy), point )
                    if minDistance < distance:
                        distance = minDistance

                # Add line to lines if min distance from point to line does not cause
                # obstacle collision.
                if distance > minCollisionDistance:
                    lines.append( (pathNode, pathNodeCopy) )

    ### YOUR CODE GOES ABOVE HERE ###
    return lines
