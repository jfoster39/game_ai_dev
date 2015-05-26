import sys, pygame, math, numpy, random, time, copy
from pygame.locals import * 

from constants import *
from utils import *
from core import *
from randomnavigator import *
from mybuildpathnetwork import *

pathnodes = [(100, 200), (800, 800), (100, 800), (800, 200)]
			
			
nav = RandomNavigator()
			
			
world = GameWorld(SEED, (1000, 1000), (1000, 1000))
agent = Agent(AGENT, (200, 200), 0, SPEED, world)
world.initializeTerrain([[(180, 420), (360, 275), (680, 371), (630, 660), (380, 697)]]) 
world.setPlayerAgent(agent)
nav.setWorld(world)
agent.setNavigator(nav)
world.initializeRandomResources(NUMRESOURCES)
world.debugging = True
for n in pathnodes:
	drawCross(world.debug, n)
nav.pathnodes = pathnodes
nav.pathnetwork = myBuildPathNetwork(pathnodes, world, agent)
nav.drawPathNetwork(world.debug)
world.run()
