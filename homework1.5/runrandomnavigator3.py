import sys, pygame, math, numpy, random, time, copy
from pygame.locals import * 

from constants import *
from utils import *
from core import *
from randomnavigator import *
from mybuildpathnetwork import *

pathnodes = [(200, 100), (900, 100), (950, 290), (75, 400), (375, 575), (200, 700), (900, 800), (900, 950), (600, 950)]
			
			
nav = RandomNavigator()
	
			
world = GameWorld(SEED, (1000, 1000), (1000, 1000))
agent = Agent(AGENT, (200, 100), 0, SPEED, world)
world.initializeTerrain([[(5, 160), (670, 260), (5, 320)],
                         [(5, 475), (265, 575), (5, 595)],
                         [(5, 800), (640, 870), (5, 960)],
                         [(974, 320), (220, 440), (560, 560), (380, 650), (974, 650)]])
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
