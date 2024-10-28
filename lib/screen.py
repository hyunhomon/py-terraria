import random, json

from lib.character import Character
from lib.ui.main_screen import MainScreen
from lib.ui.char_screen import CharScreen

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
            create_char_callback=lambda: self.create_char()
        )

        self.screen_states = {
            "main": self.main_screen,
            "char": self.char_screen
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
