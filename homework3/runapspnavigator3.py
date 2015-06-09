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
agent = Agent(AGENT, (500, 500), 0, SPEED, world)
world.initializeTerrain([[(320, 110), (480, 200), (370, 400), (100, 435), (180, 250)],
						 [(740, 160), (940, 450), (800, 540), (600, 410)],
						 [(285, 550), (400, 755), (150, 745)],
						 [(590, 750), (910, 720), (925, 870), (580, 870)]])
world.setPlayerAgent(agent)
nav.setWorld(world)
agent.setNavigator(nav)
world.initializeResources([(200, 500), (250, 800), (750, 900), (850, 650), (700, 530), (900, 250), (925, 100), (825, 175), (150, 150)], RESOURCE)
world.debugging = True

g = NearestGatherer(NPC, (50, 50), 0.0, SPEED, world)
nav2 = cloneAPSPNavigator(nav)
g.setNavigator(nav2)
g.setTargets(map(getLocation, list(world.resources)))
world.addNPC(g)
g.start()

world.run()
