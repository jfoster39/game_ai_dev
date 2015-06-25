import sys, pygame, math, numpy, random, time, copy
from pygame.locals import *

from constants import *
from utils import *
from core import *
from moba import *

class MyMinion(Minion):

	def __init__(self, position, orientation, world, image = NPC, speed = SPEED, viewangle = 360, hitpoints = HITPOINTS, firerate = FIRERATE, bulletclass = SmallBullet):
		Minion.__init__(self, position, orientation, world, image, speed, viewangle, hitpoints, firerate, bulletclass)
		self.states = [Idle]
		### Add your states to self.states (but don't remove Idle)
		### YOUR CODE GOES BELOW HERE ###

		self.states.append(AttackMinion)
		self.states.append(AttackTower)

		### YOUR CODE GOES ABOVE HERE ###

	def start(self):
		Minion.start(self)
		self.changeState(Idle)





############################
### Idle
###
### This is the default state of MyMinion. The main purpose of the Idle state is to figure out what state to change to and do that immediately.

class Idle(State):

	def enter(self, oldstate):
		State.enter(self, oldstate)
		# stop moving
		self.agent.stopMoving()

	def execute(self, delta = 0):
		State.execute(self, delta)
		### YOUR CODE GOES BELOW HERE ###

		self.agent.changeState(AttackTower)

		### YOUR CODE GOES ABOVE HERE ###
		return None

##############################
### Taunt
###
### This is a state given as an example of how to pass arbitrary parameters into a State.
### To taunt someome, Agent.changeState(Taunt, enemyagent)

class Taunt(State):

	def parseArgs(self, args):
		self.victim = args[0]

	def execute(self, delta = 0):
		if self.victim is not None:
			print "Hey " + str(self.victim) + ", I don't like you!"
		self.agent.changeState(Idle)

##############################
### YOUR STATES GO HERE:o

class AttackTower(State):

	# Get towers/bases and navigate to the closest one.
	def enter(self, oldstate):
		self.enemyTowers  = self.agent.world.getEnemyTowers(self.agent.getTeam())
		self.enemyTowers  = sorted(self.enemyTowers, key=lambda tower: distance(self.agent.getLocation(), tower.getLocation() ))
		self.enemyTowers += self.enemyTowers + self.agent.world.getEnemyBases(self.agent.getTeam())
		self.agent.navigateTo(self.enemyTowers[0].getLocation())

	def execute(self, delta = 0):
		State.execute(self, delta)
		minions = self.agent.getVisibleType(Minion)

		# If we are close to tower go ahead and attack it.
		if distance(self.agent.getLocation(), self.enemyTowers[0].getLocation()) < TOWERBULLETRANGE:
			if distance(self.agent.getLocation(), self.enemyTowers[0].getLocation()) < SMALLBULLETRANGE:
				self.agent.turnToFace(self.enemyTowers[0].getLocation())
				self.agent.shoot()
				if self.enemyTowers[0].isAlive() == False:
					self.enemyTowers.pop(0)
					if self.enemyTowers:
						self.agent.changeState(Idle)

		# If there are visible minions, find enemies, then find closest enemy, then attack that enemy.
		elif minions:
			enemyMinions = []
			for minion in minions:
				if minion.getTeam() != self.agent.getTeam():
					enemyMinions.append(minion)

			if enemyMinions:
				enemyMinions   = sorted(enemyMinions, key=lambda enemy: distance( self.agent.getLocation(), enemy.getLocation() ))
				minionToAttack = enemyMinions[0]
				self.agent.changeState(AttackMinion, minionToAttack)

	def exit(self):
		State.exit(self)

class AttackMinion(State):

	def parseArgs(self, args):
		self.minion = args[0]

	def enter(self, oldstate):
		State.enter(self, oldstate)

	def execute(self, delta = 0):
		State.execute(self, delta)
		if self.minion.isAlive():
			self.agent.navigateTo(self.minion.getLocation())
			if distance( self.agent.getLocation(), self.minion.getLocation() ) < SMALLBULLETRANGE:
				self.agent.turnToFace(self.minion.getLocation())
				self.agent.shoot()
			else:
				self.agent.changeState(AttackTower)
		else:
			self.agent.changeState(AttackTower)


