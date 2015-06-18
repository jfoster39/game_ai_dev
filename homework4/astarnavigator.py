import sys, pygame, math, numpy, random, time, copy
from pygame.locals import *

from constants import *
from utils import *
from core import *
from mycreatepathnetwork import *
from mynavigatorhelpers import *


###############################
### AStarNavigator
###
### Creates a path node network and implements the FloydWarshall all-pairs shortest-path algorithm to create a path to the given destination.

class AStarNavigator(NavMeshNavigator):

	def __init__(self):
		Navigator.__init__(self)


	### Create the pathnode network and pre-compute all shortest paths along the network.
	### self: the navigator object
	### world: the world object
	def createPathNetwork(self, world):
		self.pathnodes, self.pathnetwork, self.navmesh = myCreatePathNetwork(world, self.agent)
		return None

	### Finds the shortest path from the source to the destination using A*.
	### self: the navigator object
	### source: the place the agent is starting from (i.e., it's current location)
	### dest: the place the agent is told to go to
	def computePath(self, source, dest):
		### Make sure the next and dist matricies exist
		if self.agent != None and self.world != None:
			self.source = source
			self.destination = dest
			### Step 1: If the agent has a clear path from the source to dest, then go straight there.
			###   Determine if there are no obstacles between source and destination (hint: cast rays against world.getLines(), check for clearance).
			###   Tell the agent to move to dest
			### Step 2: If there is an obstacle, create the path that will move around the obstacles.
			###   Find the pathnodes closest to source and destination.
			###   Create the path by traversing the self.next matrix until the pathnode closes to the destination is reached
			###   Store the path by calling self.setPath()
			###   Tell the agent to move to the first node in the path (and pop the first node off the path)
			if clearShot(source, dest, self.world.getLines(), self.world.getPoints(), self.agent):
				self.agent.moveToTarget(dest)
			else:
				start = findClosestUnobstructed(source, self.pathnodes, self.world.getLinesWithoutBorders())
				end = findClosestUnobstructed(dest, self.pathnodes, self.world.getLinesWithoutBorders())
				if start != None and end != None:
					newnetwork = unobstructedNetwork(self.pathnetwork, self.world.getGates())
					closedlist = []
					path, closedlist = astar(start, end, newnetwork)
					if path is not None and len(path) > 0:
						path = shortcutPath(source, dest, path, self.world, self.agent)
						self.setPath(path)
						if self.path is not None and len(self.path) > 0:
							first = self.path.pop(0)
							self.agent.moveToTarget(first)
		return None

	### Called when the agent gets to a node in the path.
	### self: the navigator object
	def checkpoint(self):
		myCheckpoint(self)
		return None

	### This function gets called by the agent to figure out if some shortcutes can be taken when traversing the path.
	### This function should update the path and return True if the path was updated.
	def smooth(self):
		return mySmooth(self)

	def update(self, delta):
		myUpdate(self, delta)


def unobstructedNetwork(network, worldLines):
	newnetwork = []
	for l in network:
		hit = rayTraceWorld(l[0], l[1], worldLines)
		if hit == None:
			newnetwork.append(l)
	return newnetwork


def getLowest( open, f_score ):
	lowest 	   = INFINITY
	lowestNode = None
	for node in open:
		if f_score[node] < lowest:
			lowest 	   = f_score[node]
			lowestNode = node
	return lowestNode

def reconstructPath( cameFrom, goal ):
	path = [goal]
	while goal in cameFrom:
		goal = cameFrom[goal]
		path.append( goal )
	path = path[::-1]
	return path

def astar(init, goal, network):
	path     = []
	open     = []
	closed   = []
	g_score  = {}
	f_score  = {}
	cameFrom = {}
	### YOUR CODE GOES BELOW HERE ###
	open.append( init );

	g_score[init] = 0
	f_score[init] = g_score[init] + distance( init, goal )

	while open:
		current = getLowest( open, f_score )
		if current == goal:
			path = reconstructPath( cameFrom, goal )
			return path, closed

		open.remove( current )
		closed.append( current )

		for index, edge in enumerate( network ):
			if current in network[index]:
				if current == edge[0]:
					neighbor = edge[1]
				else:
					neighbor = edge[0]

				rolling_g_score = g_score[current] + distance( current, neighbor )

				if neighbor in closed and rolling_g_score >= g_score[neighbor]:
					continue

				if neighbor not in closed or rolling_g_score < g_score[neighbor]:
					cameFrom[neighbor] = current
					g_score[neighbor]  = rolling_g_score
					f_score[neighbor]  = g_score[neighbor] + distance( neighbor, goal )

					if neighbor not in open:
						open.append( neighbor )

	return path, closed

def myUpdate(nav, delta):
	### YOUR CODE GOES BELOW HERE ###

	### YOUR CODE GOES ABOVE HERE ###
	return None



def myCheckpoint(nav):
	### YOUR CODE GOES BELOW HERE ###
	lines = nav.world.getLines()
	path  = nav.path

	if len( path ) < 1:
		return None

	for i, node in enumerate( path ):
		if i+2 == len( path ):
			return None
		hit = rayTraceWorld( path[i], path[i+1], lines )
		if hit != None:
			nav.computePath( nav.source, nav.destination )
			return None

	### YOUR CODE GOES ABOVE HERE ###
	return None
