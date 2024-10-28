from entity import Entity

class Player(Entity):
    item_selected = 0

    def __init__(self):
        super().__init__()
    
    def inventory(self):
        pass

    def interaction(self):
        pass
