import random
from localization import _

def getMsg(key):
	return _.get_translation(key)

class Player:
	def __init__(self,_id,_name):
		self.id=_id
		self.name=_name
	def playerDamage(self,_source,_value):
		# print(_source.name+" damaged "+self.name+" "+str(_value)+" point(s)!")
		print(getMsg("damage.msg")%(_source.name,self.name,str(_value)))

class Card:
	def __init__(self,_id,_mass,_thot,_size):
		self.id=_id
		self.mass=_mass
		self.thot=_thot
		self.size=_size

p1=Player(1,"雀")
p2=Player(2,"量")

p1.playerDamage(p2,5)

print(getMsg("papedream"))
