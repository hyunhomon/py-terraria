import sys, time, pygame

GAME_TITLE = "py-terraria"

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500

def main():
    pygame.init()
    pygame.display.set_caption(GAME_TITLE)

    clock = pygame.time.Clock()
    display = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT], False)

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: run = False
            else: pass # event call
        
        pygame.display.update()
        # display draw call
    
    pygame.quit()
    return

if __name__ == "__main__":
    main()
    sys.exit()
