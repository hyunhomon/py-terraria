import random, json, math, pygame

color_map = {
    0: (0, 0, 0),  # 용암
    1: (139, 69, 19),  # 흙
    2: (0, 255, 0),  # 나무
    3: (128, 128, 128),  # 돌
    4: (0, 0, 255),  # 물
    5: (255, 255, 0),  # 모래
    6: (255, 0, 0),  # 불
    7: (184, 115, 51),  # 구리
    8: (255, 255, 255)  # 철
}

class World:
    def __init__(self, name:str, auto_create:bool=True):
        self.name = name
        self.map = []
        self.width = 3000
        self.height = 1000
        self.tile_size = 1
        if auto_create:
            self.create()

    def create(self):
        # 초기화: 모든 타일을 빈 공간으로 설정
        self.map = [[0 for _ in range(self.width)] for _ in range(self.height)]
        
        # 바다 생성
        sea_depth = self.width // 10
        for x in range(self.width):
            if x < sea_depth or x >= self.width - sea_depth:  # 양쪽 끝에 바다
                depth = int((math.cos(x / (self.width / (2 * math.pi))) + 1) * 10)
                for y in range(depth):
                    if y < self.height:
                        self.map[y][x] = 4  # 물로 채움

        # 흙, 돌, 용암 설정
        for x in range(self.width):
            # 높이값을 랜덤으로 설정
            ground_height = int((random.random() * 0.1 + 0.3) * self.height)  # 0.3~0.4 범위의 높이
            for y in range(ground_height):
                if y < self.height:
                    self.map[y][x] = 1  # 흙
            for y in range(ground_height, int(ground_height + self.height * 0.3)):
                if y < self.height:
                    self.map[y][x] = 3  # 돌
            for y in range(int(ground_height + self.height * 0.3), self.height):
                if y < self.height:
                    self.map[y][x] = 0  # 용암

        # 언덕 생성
        for x in range(0, self.width, random.randint(40, 60)):
            if sea_depth < x < self.width - sea_depth:
                hill_base_height = random.randint(max(0, ground_height - 15), min(self.height, ground_height + 15))
                for h in range(-15, 16):  # ±15 범위
                    if 0 <= hill_base_height + h < self.height:
                        self.map[hill_base_height + h][x] = 1  # 언덕

        # 호수 생성
        for _ in range(random.randint(3, 5)):  # 3~5개의 호수 생성
            lake_x = random.randint(sea_depth, self.width - sea_depth)
            lake_y = random.randint(int(ground_height * 0.7), int(ground_height * 0.9))
            lake_width = random.randint(25, 35)
            lake_depth = random.randint(10, 20)

            for lx in range(lake_width):
                for ly in range(lake_depth):
                    if 0 <= lake_x + lx < self.width and 0 <= lake_y + ly < self.height:
                        self.map[lake_y + ly][lake_x + lx] = 4  # 물로 채움

        # 동굴 생성
        for _ in range(50):  # 동굴 생성 수
            cave_x = random.randint(0, self.width - 1)
            cave_y = random.randint(ground_height + 1, self.height - 1)
            radius = random.randint(40, 50)
            for cx in range(cave_x - radius, cave_x + radius + 1):
                for cy in range(cave_y - radius, cave_y + radius + 1):
                    if 0 <= cx < self.width and 0 <= cy < self.height:
                        if (cx - cave_x) ** 2 + (cy - cave_y) ** 2 <= radius ** 2:
                            self.map[cy][cx] = 0  # 동굴을 공기로

        # 광맥 생성
        for _ in range(100):  # 광맥 생성 수
            copper_x = random.randint(0, self.width - 1)
            copper_y = random.randint(ground_height + 1, self.height - 1)
            copper_radius = random.randint(10, 15)
            for cx in range(copper_x - copper_radius, copper_x + copper_radius + 1):
                for cy in range(copper_y - copper_radius, copper_y + copper_radius + 1):
                    if 0 <= cx < self.width and 0 <= cy < self.height:
                        if (cx - copper_x) ** 2 + (cy - copper_y) ** 2 <= copper_radius ** 2:
                            if self.map[cy][cx] == 3:  # 돌이 있을 때만 구리를 추가
                                self.map[cy][cx] = 7  # 구리

            iron_x = random.randint(0, self.width - 1)
            iron_y = random.randint(ground_height + 1, self.height - 1)
            iron_radius = random.randint(6, 10)
            for ix in range(iron_x - iron_radius, iron_x + iron_radius + 1):
                for iy in range(iron_y - iron_radius, iron_y + iron_radius + 1):
                    if 0 <= ix < self.width and 0 <= iy < self.height:
                        if (ix - iron_x) ** 2 + (iy - iron_y) ** 2 <= iron_radius ** 2:
                            if self.map[iy][ix] == 3:  # 돌이 있을 때만 철을 추가
                                self.map[iy][ix] = 8  # 철

    def to_json(self):
        return {
            "name": self.name,
            "map": self.map,
            "width": self.width,
            "height": self.height,
            "tile_size": self.tile_size
        }
    
    @staticmethod
    def create_from_json(json):
        world = World(json["name"], auto_create=False)
        world.map = json["map"]
        world.width = json["width"]
        world.height = json["height"]
        world.tile_size = json["tile_size"]
        return world

    def __str__(self):
        st = ''
        for row in self.map:
            for tile in row:
                st += ' ' if tile == 0 else '#' if tile == 1 else '~' if tile == 4 else '^' if tile == 3 else 'O' if tile == 7 else 'I' if tile == 8 else ' '
            st += '\n'
        return st

    def draw(self, display:pygame.Surface, camera:dict):
        pass