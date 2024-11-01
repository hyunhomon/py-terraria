import random, json

from lib.character import Character
from lib.world import World
from lib.ui.main_screen import MainScreen
from lib.ui.char_screen import CharScreen
from lib.ui.world_screen import WorldScreen
from lib.ui.game_screen import GameScreen

class Screen:
    screen_state = "main"

    def __init__(self, display):
        random_bg = random.randint(1, 12)
        
        self.main_screen = MainScreen(
            display, random_bg,
            start_game_callback=lambda: self.set_screen("char"),
            multiple_play_callback=lambda: self.set_screen("multi"),
            settings_callback=lambda: self.set_screen("settings"),
            credits_callback=lambda: self.set_screen("credits")
        )
        self.char_screen = CharScreen(
            display, random_bg,
            back_callback=lambda: self.set_screen("main"),
            create_char_callback=lambda: self.create_char(),
            goto_world_callback=lambda: self.set_screen("world")
        )
        self.world_screen = WorldScreen(
            display, random_bg,
            back_callback=lambda: self.set_screen("char"),
            create_world_callback=lambda: self.create_world(),
            play_callback=lambda: self.set_screen("game")
        )
        self.game_screen = GameScreen(display)

        self.screen_states:dict = {
            "main": self.main_screen,
            "char": self.char_screen,
            "world": self.world_screen,
            "game": self.game_screen
        }

    def event(self, event):
        self.screen_states[self.screen_state].handle_events(event)
    
    def draw(self):
        self.screen_states[self.screen_state].draw()
    
    def set_screen(self, screen):
        self.screen_state = screen
    
    def create_char(self):
        new_char = Character("Player1")
        f = open("saves/char1.json", "w")
        f.write(json.dumps(new_char.to_json(), indent=4))
        f.close()

    def create_world(self):
        new_world = World("World1")
        f = open("saves/world1.json", "w")
        f.write(json.dumps(new_world.to_json(), indent=4))
        f.close()
