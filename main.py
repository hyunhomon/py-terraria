import sys, time, pygame, random, json
from lib.ui.main_screen import MainScreen
from lib.ui.char_screen import CharScreen
from lib.character import Character

GAME_TITLE = "py-terraria"

def main():
    pygame.init()
    pygame.display.set_caption(GAME_TITLE)

    FPS = 60
    info = pygame.display.Info()
    clock = pygame.time.Clock()
    display = pygame.display.set_mode((info.current_w, info.current_h), pygame.RESIZABLE)
    run = True

    screen_state = "main"
    random_bg = random.randint(1, 12)

    main_screen = MainScreen(display, random_bg,
                             start_game_callback=lambda: set_screen("char"),
                             multiple_play_callback=lambda: set_screen("multi"),
                             settings_callback=lambda: set_screen("settings"),
                             credits_callback=lambda: set_screen("credits")
                            )
    char_screen = CharScreen(display, random_bg,
                             back_callback=lambda: set_screen("main"),
                             create_char_callback=lambda: create_char()
                            )

    def set_screen(screen):
        nonlocal screen_state
        screen_state = screen
    
    def create_char():
        new_char = Character("Player1")
        f = open("saves/char1.json", "w")
        f.write(json.dumps(new_char.to_json(), indent=4))
        f.close()

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: run = False
            elif screen_state == "main":
                main_screen.handle_events(event)
            elif screen_state == "char":
                char_screen.handle_events(event)

        if screen_state == "main":
            main_screen.draw()
        elif screen_state == "char":
            char_screen.draw()
        
        pygame.display.update()
        # display draw call
        clock.tick(FPS)
    
    pygame.quit()
    return

if __name__ == "__main__":
    main()
    sys.exit()
