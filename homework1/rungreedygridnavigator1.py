import sys, pygame, math, numpy, random, time, copy
from pygame.locals import *

from constants import *
from utils import *
from core import *
from gridnavigator import *




nav = GreedyGridNavigator()


world = GameWorld(SEED, WORLD, SCREEN)
agent = Agent(AGENT, (SCREEN[0]/2, SCREEN[1]/2), 0, SPEED, world)
world.initializeTerrain([[(628, 698), (582, 717), (549, 688), (554, 546), (676, 548)], [(942, 484), (811, 396), (843, 299), (921, 300)], [(457, 422), (371, 506), (300, 515), (300, 400), (454, 350)]], (0, 0, 0), 4, TREE)
world.setPlayerAgent(agent)
agent.setNavigator(nav)
nav.setWorld(world)
world.initializeRandomResources(NUMRESOURCES)
world.debugging = True
world.run()
