import sys, pygame, math, numpy, random, time, copy
from pygame.locals import * 

from constants import *
from utils import *
from core import *
from apspnavigator import *
from nearestgatherer import *

def getLocation(mover):
	return mover.getLocation()
	
	
def cloneAPSPNavigator(nav):
	newnav = APSPNavigator()
	newnav.world = nav.world
	newnav.pathnodes = nav.pathnodes
	newnav.pathnetwork = nav.pathnetwork
	newnav.next = nav.next
	newnav.dist = nav.dist
	return newnav
			
nav = APSPNavigator()
			
			
world = GameWorld(SEED, (1000, 1000), (1000, 1000))
agent = Agent(AGENT, (200, 200), 0, SPEED, world)
world.initializeTerrain([[(180, 420), (360, 275), (680, 371), (630, 660), (380, 697)]])
world.setPlayerAgent(agent)
nav.setWorld(world)
agent.setNavigator(nav)
world.initializeResources([(220, 575), (550, 700), (700, 500), (900, 300)], RESOURCE)
world.debugging = True

g = NearestGatherer(NPC, (50, 50), 0.0, SPEED, world)
nav2 = cloneAPSPNavigator(nav)
g.setNavigator(nav2)
g.setTargets(map(getLocation, list(world.resources)))
world.addNPC(g)
g.start()

world.run()
