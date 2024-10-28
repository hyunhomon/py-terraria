from abc import ABC, abstractmethod
from typing import List, Literal
from .item import Item

class Block(ABC):
    @property
    @abstractmethod
    def id(self) -> int:
        return 0

    @property
    @abstractmethod
    def hardness(self) -> int:
        return 0
    
    @property
    @abstractmethod
    def drop_item(self) -> Item:
        return None