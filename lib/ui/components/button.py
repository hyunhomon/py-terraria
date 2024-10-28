import pygame

class Button:
    def __init__(self, text, pos, font:pygame.font.Font, bg_color=(255, 255, 255, 255), text_color=(0, 0, 0, 255), border_radius=10, padding=(100, 10)):
        self.text = text
        self.font = font
        self.bg_color = bg_color
        self.text_color = text_color
        self.border_radius = border_radius
        self.is_hovered = False  # Hover 상태
        self.padding = padding

        # 버튼 위치 설정
        self.rect = None
        self.update_text()  # 텍스트와 rect 초기화
        self.rect.center = pos

    def update_text(self):
        # 텍스트 표면 생성
        text_surface = self.font.render(self.text, True, self.text_color[:3])
        text_surface.set_alpha(self.text_color[3])
        self.text_surface = text_surface

        self.rect = text_surface.get_rect()  # 텍스트 rect 가져오기
        self.rect.inflate_ip(self.padding[0], self.padding[1])

    def draw(self, screen):
        # 배경 Surface 생성
        bg_surface = pygame.Surface(self.rect.size, pygame.SRCALPHA)  # 알파 채널을 가진 Surface 생성
        bg_surface.fill((0, 0, 0, 0))  # 투명한 배경으로 초기화
        # 버튼 그리기
        pygame.draw.rect(bg_surface, self.bg_color, bg_surface.get_rect(), border_radius=self.border_radius)

        # 배경을 메인 화면에 그리기
        screen.blit(bg_surface, self.rect.topleft)

        # 텍스트를 버튼 중앙에 그리기
        text_rect = self.text_surface.get_rect(center=self.rect.center)
        screen.blit(self.text_surface, text_rect.topleft)

    def is_clicked(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)
