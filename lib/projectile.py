from abc import ABC, abstractmethod
from typing import List, Literal

class Projectile(ABC):
    @property
    @abstractmethod
    def id(self) -> int:
        return 0

    @property
    @abstractmethod
    def damage(self) -> int:
        return 1
    
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
    def affected_by_gravity(self) -> bool:
        return False
    
    @property
    @abstractmethod
    def max_penetration(self) -> int:
        return 1
    
    @property
    @abstractmethod
    def ignore_tile_collision(self) -> bool:
        return False

    @property
    def penetration(self) -> int:
        return 1

    @property
    def max_time(self) -> int: # ms
        return 60000

    @property
    def position(self) -> tuple:
        return (0, 0)
    
    @property
    def velocity(self) -> tuple:
        return (0, 0)
    
    @property
    def rotation(self) -> float: # degrees (radians)
        return 0