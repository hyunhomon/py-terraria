import pygame, json
from lib.ui.components.button import Button
from lib.ui.components.box import Box
from lib.character import Character

class CharScreen:
    def __init__(self, display: pygame.Surface, random_bg: int,
                 back_callback: callable,
                 create_char_callback: callable
                ):
        self.display = display
        self.font = pygame.font.Font("fonts/ANDYB.TTF", 48)
        self.map_bg_int = random_bg
        self.logo = pygame.image.load("assets/Logo.png")
        self.back_callback = back_callback
        self.create_char_callback = create_char_callback

        # 박스 생성
        self.frame = Box((self.display.get_width() // 2, self.display.get_height() // 2 + 80), (600, 700), bg_color=(80, 80, 200, 200), border_radius=10, padding=(100, 10))

        # 타이틀 생성
        self.title = Button("Create Character", (self.display.get_width() // 2, 250), self.font, bg_color=(80, 80, 200, 255), text_color=(255, 255, 255, 255),
                            border_radius=10, padding=(100, 10))

        # 버튼 생성
        self.back_button = Button("Back", (self.display.get_width() // 2 - 120, self.display.get_height() - 100), self.font,
                                   bg_color=(80, 80, 200, 255), text_color=(255, 255, 255, 225), border_radius=10, padding=(100, 10))
        self.create_char_button = Button("Create", (self.display.get_width() // 2 + 120, self.display.get_height() - 100), self.font,
                                      bg_color=(80, 80, 200, 255), text_color=(255, 255, 255, 225), border_radius=10, padding=(100, 10))
        self.play_button = Button("Play", (self.display.get_width() // 2, self.display.get_height() // 2 + 100), self.font,
                                  bg_color=(80, 80, 200, 255), text_color=(255, 255, 255, 255), border_radius=10, padding=(100, 10))
        
        self.char = None
        self.call_char()

    def handle_events(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.back_button.is_clicked(event.pos):
                self.back_callback()
            elif self.create_char_button.is_clicked(event.pos):
                self.create_char_callback()
                self.call_char()
            elif self.play_button.is_clicked(event.pos):
                print("Play button clicked")

    def call_char(self):
        f = open("saves/char1.json", "r")
        r = f.read()
        if r == "":
            f.close()
            return
        else:
            json_data = json.loads(r)
            f.close()
            if json_data:
                self.char = Character.create_from_json(json_data)

    def draw(self):
        self.display.fill((0, 0, 0))
        bg_img = pygame.image.load(f"assets/MapBG{self.map_bg_int}.png")
        bg_img = pygame.transform.scale(bg_img, (self.display.get_width(), self.display.get_height()))
        self.display.blit(bg_img, (0, 0))
        self.display.blit(self.logo, (self.display.get_width() // 2 - self.logo.get_width() // 2, 50))
        self.frame.draw(self.display)
        self.title.draw(self.display)
        self.back_button.draw(self.display)
        self.create_char_button.draw(self.display)
        if self.char:
            _box = Box((self.display.get_width() // 2, self.display.get_height() // 2), (400, 400), bg_color=(80, 80, 200, 200), border_radius=10, padding=(100, 10))
            _char_name = Button(self.char.name, (self.display.get_width() // 2, self.display.get_height() // 2 - 150), self.font, bg_color=(80, 80, 200, 255), text_color=(255, 255, 255, 255), border_radius=10, padding=(100, 10))
            _char_hp = Button(f"HP: {self.char.hp}/{self.char.max_hp}", (self.display.get_width() // 2, self.display.get_height() // 2 - 90), self.font, bg_color=(80, 80, 200, 255), text_color=(255, 255, 255, 255), border_radius=10, padding=(100, 10))
            _char_mp = Button(f"MP: {self.char.mp}/{self.char.max_mp}", (self.display.get_width() // 2, self.display.get_height() // 2 - 30), self.font, bg_color=(80, 80, 200, 255), text_color=(255, 255, 255, 255), border_radius=10, padding=(100, 10))
            _box.draw(self.display)
            _char_name.draw(self.display)
            _char_hp.draw(self.display)
            _char_mp.draw(self.display)
            self.play_button.draw(self.display)