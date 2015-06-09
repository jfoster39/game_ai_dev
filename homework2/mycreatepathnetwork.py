import sys, pygame, math, numpy, random, time, copy, operator
from pygame.locals import *

from constants import *
from utils import *
from core import *

# Creates a pathnode network that connects the midpoints of each navmesh together
def myCreatePathNetwork(world, agent = None):
	nodes  		= []
	edges  		= []
	polys  		= []
	points 		= world.getPoints()
	pointsCopy 	= copy.copy( points )
	### YOUR CODE GOES BELOW HERE ###

	# Find convex hulls
	# Randomly pick points on obstacles and exhaustively find all
	# triangles from that point, then move on to the next random point.

	for point in points :
		for pointCopy in pointsCopy :


	### YOUR CODE GOES ABOVE HERE ###
	return nodes, edges, polys


