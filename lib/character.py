from lib.inventory import Inventory

class Character:
    def __init__(self, name: str):
            self.name = name
            self.max_hp = 100
            self.max_mp = 20
            self.hp = 100
            self.mp = 20
            self.attack = 1 # multiplier
            self.defense = 0
            self.speed = 1
            self.jump = 3
            self.inventory = Inventory()
    
    def to_json(self):
        return {
            "name": self.name,
            "max_hp": self.max_hp,
            "max_mp": self.max_mp,
            "hp": self.hp,
            "mp": self.mp,
            "attack": self.attack,
            "defense": self.defense,
            "speed": self.speed,
            "jump": self.jump,
            "inventory": self.inventory.to_json()
        }
    
    @staticmethod
    def create_from_json(json):
        char = Character(json["name"])
        char.max_hp = json["max_hp"]
        char.max_mp = json["max_mp"]
        char.hp = json["hp"]
        char.mp = json["mp"]
        char.attack = json["attack"]
        char.defense = json["defense"]
        char.speed = json["speed"]
        char.jump = json["jump"]
        char.inventory = Inventory.create_from_json(json["inventory"])
        return char