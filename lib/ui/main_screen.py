import pygame, sys, random
from lib.ui.components.button import Button

class MainScreen:
    def __init__(self, display: pygame.Surface, random_bg: int,
                 start_game_callback: callable,
                 multiple_play_callback: callable,
                 settings_callback: callable,
                 credits_callback: callable
                ):
        self.display = display
        self.font = pygame.font.Font("fonts/ANDYB.TTF", 48)
        self.map_bg_int = random_bg
        self.logo = pygame.image.load("assets/Logo.png")
        self.start_game_callback = start_game_callback
        self.multiple_play_callback = multiple_play_callback
        self.settings_callback = settings_callback
        self.credits_callback = credits_callback

        start_y = 350
        gap_y = 90

        # 버튼 생성
        self.start_button = Button("Single Play", (self.display.get_width() // 2, start_y + (gap_y * 0)), self.font,
                                   bg_color=(0, 0, 0, 0), text_color=(255, 255, 255, 255))
        self.multi_button = Button("Multi Play", (self.display.get_width() // 2, start_y + (gap_y * 1)), self.font,
                                   bg_color=(0, 0, 0, 0), text_color=(255, 255, 255, 255))
        self.settings_button = Button("Settings", (self.display.get_width() // 2, start_y + (gap_y * 2)), self.font,
                                   bg_color=(0, 0, 0, 0), text_color=(255, 255, 255, 255))
        self.credits_button = Button("Credits", (self.display.get_width() // 2, start_y + (gap_y * 3)), self.font,
                                   bg_color=(0, 0, 0, 0), text_color=(255, 255, 255, 255))
        self.quit_button = Button("Quit", (self.display.get_width() // 2, start_y + (gap_y * 4)), self.font,
                                  bg_color=(0, 0, 0, 0), text_color=(255, 255, 255, 255))

    def handle_events(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.start_button.is_clicked(event.pos):
                self.start_game_callback()
            elif self.multi_button.is_clicked(event.pos):
                self.multiple_play_callback()
            elif self.settings_button.is_clicked(event.pos):
                self.settings_callback()
            elif self.credits_button.is_clicked(event.pos):
                self.credits_callback()
            elif self.quit_button.is_clicked(event.pos):
                pygame.quit()
                exit()  # 프로그램 종료

    def draw(self):
        self.display.fill((0, 0, 0))
        bg_img = pygame.image.load(f"assets/MapBG{self.map_bg_int}.png")
        bg_img = pygame.transform.scale(bg_img, (self.display.get_width(), self.display.get_height()))
        self.display.blit(bg_img, (0, 0))
        self.display.blit(self.logo, (self.display.get_width() // 2 - self.logo.get_width() // 2, 50))
        self.start_button.draw(self.display)
        self.multi_button.draw(self.display)
        self.settings_button.draw(self.display)
        self.credits_button.draw(self.display)
        self.quit_button.draw(self.display)