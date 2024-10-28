import sys, pygame
from lib.screen import Screen

GAME_TITLE = "py-terraria"

def main():
    pygame.init()
    pygame.display.set_caption(GAME_TITLE)

    FPS = 60
    info = pygame.display.Info()
    clock = pygame.time.Clock()
    time = clock.tick(FPS)
    display = pygame.display.set_mode((info.current_w, info.current_h), pygame.RESIZABLE)
    screen = Screen(display)
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: running = False
            screen.event(event)
        
        screen.draw()
        pygame.display.update()
    
    pygame.quit()
    return

if __name__ == "__main__":
    main()
    sys.exit()
