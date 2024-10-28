from abc import ABC, abstractmethod
from typing import List, Literal

Tag = Literal["consumable", "buildable", "material", "ammunition", "tool"]

class Item(ABC):
    @property
    @abstractmethod
    def id(self) -> int:
        return 0
    
    @property
    @abstractmethod
    def name(self) -> str:
        return "Item name"
    
    @property
    @abstractmethod
    def description(self) -> str:
        return "Item description"
    
    @property
    def stack(self) -> int:
        return 1

    @property
    @abstractmethod
    def max_stack(self) -> int:
        return 9999
    
    @property
    @abstractmethod
    def tags(self) -> List[Tag]:
        return []

    @abstractmethod
    def use(self):
        pass