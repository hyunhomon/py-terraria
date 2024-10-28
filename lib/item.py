from abc import ABC, abstractmethod
from typing import List, Literal
from lib.items.tool import Tool
from lib.items.tools.pickaxe import Pickaxe
from lib.items.tools.axe import Axe
from lib.items.tools.hammer import Hammer

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

    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "stack": self.stack,
            "max_stack": self.max_stack,
            "tags": self.tags
        }
    
    @staticmethod
    def create_from_json(json):
        if json["pickaxe_power"] :
            return Pickaxe.create_from_json(json)
        elif json["axe_power"] :
            return Axe.create_from_json(json)
        elif json["hammer_power"] :
            return Hammer.create_from_json(json)
        elif json["damage"] :
            return Tool.create_from_json(json)