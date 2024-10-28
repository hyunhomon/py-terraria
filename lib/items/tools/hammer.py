from abc import abstractmethod
from .tool import DamageType, Tool

class Hammer(Tool):
    @property
    def damage_type(self) -> DamageType:
        return "melee"

    @property
    @abstractmethod
    def damage(self) -> int:
        return 1
    
    @property
    @abstractmethod
    def critical_chance(self) -> int:
        return 4
    
    @property
    @abstractmethod
    def speed(self) -> int:
        return 1
    
    @property
    @abstractmethod
    def knockback(self) -> int:
        return 1
    
    @property
    @abstractmethod
    def hammer_power(self) -> float:
        return 0.4

    @abstractmethod
    def hammer(self):
        pass

    @abstractmethod
    def attack(self):
        pass

    @abstractmethod
    def use(self):
        self.attack()

    @staticmethod
    def create_from_json(json):
        hammer = Hammer()
        hammer.id = json["id"]
        hammer.name = json["name"]
        hammer.description = json["description"]
        hammer.stack = json["stack"]
        hammer.max_stack = json["max_stack"]
        hammer.tags = json["tags"]
        return hammer