import pygame, json
from lib.world import World
from lib.entity import Entity
# from lib.player import Player
from lib.projectile import Projectile
from lib.ui.components.button import Button
from lib.ui.components.box import Box
from lib.character import Character
from typing import List

class GameScreen:
    def __init__(self, display: pygame.Surface):
        # load character
        char = None
        f = open("saves/char1.json", "r")
        r = f.read()
        if r == "":
            f.close()
            return
        else:
            json_data = json.loads(r)
            f.close()
            if json_data:
                char = Character.create_from_json(json_data)

        # load world
        world = None
        f = open("saves/world1.json", "r")
        r = f.read()
        if r == "":
            f.close()
            return
        else:
            json_data = json.loads(r)
            f.close()
            if json_data:
                world = World.create_from_json(json_data)

        # ui properties
        self.display = display
        self.font = pygame.font.Font("fonts/ANDYB.TTF", 48)

        # game properties
        self.world = world
        self.players:List = []
        self.entities:List[Entity] = []
        self.projectiles:List[Projectile] = []

        # self.my_player = Player(char)
        self.camera:dict = {
            "position": [0, 0],
            "rotation": 0,
            "zoom": 1
        }
    
    def handle_events(self, event):
        # if key down, move camera
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.camera["position"][0] -= 10
            elif event.key == pygame.K_RIGHT:
                self.camera["position"][0] += 10
            elif event.key == pygame.K_UP:
                self.camera["position"][1] -= 10
            elif event.key == pygame.K_DOWN:
                self.camera["position"][1] += 10

    def tick(self, delta:float):
        pass

    def draw(self):
        self.display.fill((0, 0, 0))
        self.world.draw(self.display, self.camera)
        # for entity in self.entities:
        #     entity.draw(self.display, self.camera)
        # for player in self.players:
        #     player.draw(self.display, self.camera)
        # for projectile in self.projectiles:
        #     projectile.draw(self.display, self.camera)
        # self.my_player.draw(self.display, self.camera)