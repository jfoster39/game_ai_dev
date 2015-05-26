import sys, pygame, math, numpy, random, time, copy
from pygame.locals import * 

from constants import *
from utils import *
from core import *
from randomnavigator import *
from mybuildpathnetwork import *

pathnodes = [(50, 40), (500, 50), (950, 40), (500, 500), (380, 250), (620, 250), (30, 510), (970, 510), (50, 950), (950, 950), (500, 930), (525, 275)]

			
			
nav = RandomNavigator()
			
			
world = GameWorld(SEED, (1000, 1000), (1000, 1000))
agent = Agent(AGENT, (500, 500), 0, SPEED, world)
world.initializeTerrain([[(150, 100), (390, 100), (390, 150), (295, 220), (295, 280), (390, 350), (390, 400), (150, 400)],
                         [(850, 90), (610, 90), (610, 140), (705, 210), (705, 270), (610, 340), (610, 390), (850, 390)],
                         [(100, 565), (340, 565), (340, 833), (100, 833)],
                         [(900, 585), (660, 585), (660, 813), (900, 813)]], (0, 0, 0), 4, TREE) 
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
