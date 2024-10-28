from abc import abstractmethod
from ..tool import DamageType, Tool

class Pickaxe(Tool):
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
    def pickaxe_power(self) -> float:
        return 0.4

    @abstractmethod
    def mine(self):
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