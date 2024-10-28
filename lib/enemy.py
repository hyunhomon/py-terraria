from entity import Entity

class Enemy(Entity):
    target = 0

    def __init__(self):
        super().__init__()
    
    def attack(self):
        pass
