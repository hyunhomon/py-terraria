import sys, time, pygame

GAME_TITLE = "py-terraria"

def main():
    pygame.init()
    pygame.display.set_caption(GAME_TITLE)

    info = pygame.display.Info()
    clock = pygame.time.Clock()
    display = pygame.display.set_mode((info.current_w, info.current_h), pygame.RESIZABLE)
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
