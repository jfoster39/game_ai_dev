import sys, pygame, math, numpy, random, time, copy
from pygame.locals import * 

from constants import *
from utils import *
from core import *
from randomnavigator import *
from mybuildpathnetwork import *

			
pathnodes = [(50, 50), (600, 50), (50, 550), (500, 450), (900, 175), (75, 900), (450, 950), (700, 650), (950, 650), (850, 940)]
			
nav = RandomNavigator()
	
			
world = GameWorld(SEED, (1000, 1000), (1000, 1000))
agent = Agent(AGENT, (200, 100), 0, SPEED, world)

world.initializeTerrain([[(320, 110), (480, 200), (370, 400), (100, 435), (180, 250)],
                         [(740, 160), (940, 450), (800, 540), (600, 410)],
                         [(285, 550), (400, 755), (150, 745)],
                         [(590, 750), (910, 720), (925, 870), (580, 870)]], (0, 0, 0), 4, TREE)
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
