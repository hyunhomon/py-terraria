from lib.item import Item
from typing import List

class Inventory:
    def __init__(self):
        self.items:List[Item] = []
        self.max_slots = 40

    def __len__(self):
        return len(self.items)
    
    def __str__(self) -> str:
        for item in self.items:
            print(item.name)

    def add_item(self, item:Item):
        if len(self.items) >= self.max_slots:
            return False
        else : self.items.append(item)

    def remove_item(self, item:Item):
        if item in self.items:
            self.items.remove(item)
            return True
        return False

    def get_item(self, index):
        return self.items[index]

    def find_item_by_id(self, id:int):
        for item in self.items:
            if item.id == id:
                return item
        return None
    
    def find_item_by_name(self, name:str):
        for item in self.items:
            if item.name == name:
                return item
        return None

    def to_json(self):
        return [item.to_json() for item in self.items]
    
    @staticmethod
    def create_from_json(json):
        inv = Inventory()
        inv.items = [Item.create_from_json(item) for item in json]
        return inv