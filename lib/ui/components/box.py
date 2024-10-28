import pygame

class Box:
    def __init__(self, pos, size:tuple = (100, 100), bg_color=(255, 255, 255, 255), border_radius=10, padding=(100, 10)):
        self.pos = pos
        self.size = size
        self.bg_color = bg_color
        self.border_radius = border_radius
        self.is_hovered = False  # Hover 상태
        self.padding = padding

        # 버튼 위치 설정
        self.rect = pygame.Rect(self.pos, self.size)
        self.rect.center = pos
    
    def draw(self, screen):
        # 배경 Surface 생성
        bg_surface = pygame.Surface(self.rect.size, pygame.SRCALPHA)
        bg_surface.fill((0, 0, 0, 0))
        pygame.draw.rect(bg_surface, self.bg_color, bg_surface.get_rect(), border_radius=self.border_radius)

        # 배경을 메인 화면에 그리기
        screen.blit(bg_surface, self.rect.topleft)