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

def load_language(language_code):
    """
    根据语言代码加载对应的 JSON 文件
    """
    file_path = os.path.join("locales", f"{language_code}.json")
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: Language file {file_path} not found.")
        return None

def get_localized_message(language_data, key, **kwargs):
    """
    获取本地化消息，并支持格式化
    """
    if key in language_data:
        return language_data[key].format(**kwargs)
    else:
        print(f"Warning: Key '{key}' not found in language data.")
        return ""


p1=Player(1,"雀")
p2=Player(2,"量")

p1.playerDamage(p2,5)

print("Hello Papedream!")
