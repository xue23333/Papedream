import random
import os
from localization import _

def getMsg(key):
	return _.get_translation(key)

class Player:
	def __init__(self,_id,_name):
		self.id=_id
		self.name=_name
    def useCard(self,_index,_target):
        print("")
	def playerDamage(self,_source,_value):
		# print(_source.name+" damaged "+self.name+" "+str(_value)+" point(s)!")
		print(getMsg("damage.msg")%(_source.name,self.name,str(_value)))

class Card:
	def __init__(self,_id,_mass,_thot,_size):
		self.id=_id
		self.mass=_mass
		self.thot=_thot
		self.size=_size

def Game():
	print(getMsg("game.start"))

def Version():
	print(getMsg("info.version"))

def main():
	print("请输入语言代码：",end=" ")
	_.set_locale(input())
	Version()
	p1=Player(1,getMsg("characters.1.name"))
	p2=Player(2,getMsg("characters.2.name"))
	p1.playerDamage(p2,5)
	print(getMsg("papedream"))
	Game()

	# print("Debug $",end=" ")
	# print(eval(input()))

if __name__=="__main__":
	main()
