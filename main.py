import random
import json

class Player:
	def __init__(self,_id):
		self.id=_id
	def playerDamage(self,_source,_value):
		print(_source.name+" damaged "+self.name+" "+str(_value)+" point(s)!")

class Card:
	def __init__(self,_id,_mass,_thot,_size)
		self.id=_id
		self.mass=_mass
		self.thot=_thot
		self.size=_size


p1=Player(1,"雀")
p2=Player(2,"量")

p1.playerDamage(p2,5)

print("Hello Papedream!")
