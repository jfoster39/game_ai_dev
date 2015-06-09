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
			
			
world = GameWorld(SEED, (1224, 900), (1224, 900))
agent = Agent(AGENT, (612, 450), 0, SPEED, world)
world.initializeTerrain([[(628, 698), (582, 717), (549, 688), (554, 566), (676, 548)], [(942, 484), (811, 396), (843, 299), (921, 300)], [(457, 422), (381, 490), (300, 515), (310, 400), (454, 350)]])
world.setPlayerAgent(agent)
nav.setWorld(world)
agent.setNavigator(nav)
world.initializeResources([(350,550), (750, 600), (700, 750), (1050, 300), (900, 150), (250, 300)], RESOURCE)
world.debugging = True

g = NearestGatherer(NPC, (50, 50), 0.0, SPEED, world)
nav2 = cloneAPSPNavigator(nav)
g.setNavigator(nav2)
g.setTargets(map(getLocation, list(world.resources)))
world.addNPC(g)
g.start()

world.run()
