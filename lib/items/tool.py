from abc import abstractmethod
from typing import List, Literal
from ..item import Item, Tag

DamageType = Literal["melee", "ranged", "magic", "summon", "throwing"]

class Tool(Item):
    @property
    def stack(self) -> int:
        return 1

    @property
    def max_stack(self) -> int:
        return 1

    @property
    def tags(self) -> List[Tag]:
        return ["tool"]
    
    @property
    @abstractmethod
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

    @abstractmethod
    def mine(self):
        pass

    @abstractmethod
    def chop(self):
        pass

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
    @abstractmethod
    def create_from_json(json):
        pass