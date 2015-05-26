import sys, pygame, math, numpy, random, time, copy
from pygame.locals import * 

from constants import *
from utils import *
from core import *
from randomnavigator import *
from mybuildpathnetwork import *
			
pathnodes = [(400, 600), (650, 400), (650, 200), (1075, 150), (100, 200), (100, 500), (1000, 700), (450, 800)]


			
nav = RandomNavigator()
			
			
world = GameWorld(None, (1224, 900), (1224, 900))
agent = Agent(AGENT, (SCREEN[0]/2, SCREEN[1]/2), 0, SPEED, world)
world.initializeTerrain([[(628, 698), (582, 717), (549, 688), (554, 566), (676, 548)], [(942, 484), (811, 396), (843, 299), (921, 300)], [(457, 422), (381, 490), (300, 515), (310, 400), (454, 350)]], (0, 0, 0), 4, TREE)
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

