import pygame

class Entity(pygame.sprite.Sprite):
    id = 0
    name = ""

    health = 0
    defense = 0
    damage = 0

    position = (0, 0)
    velocity = 0

    drop_item = []
    drop_gold = 0

    def __init__(self, position, assets, asset_amount):
        super(Entity, self).__init__()

        width = assets.get_width()
        height = assets.get_height()
        size = (width, height/asset_amount)

        self.time = 0
        self.rect = pygame.Rect(position, size)
        self.index = 0
        self.images = []
        for i in range(asset_amount):
            cropped = pygame.Surface(size)
            cropped.blit(assets, (0, 0), (0, size[1]*i, *size))
            self.images.append(cropped)
        self.image = self.images[self.index]
    
    def update(self, time):
        self.time += time
        if self.time > 300:
            self.time = 0
            self.index = (self.index + 1) % len(self.images)
            self.image = self.images[self.index]
