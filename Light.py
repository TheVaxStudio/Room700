import pygame

class Light:
    def __init__(self):
        self.light_surface = pygame.image.load('../Assets/Light.png').convert_alpha()
        self.ResizeLight = pygame.transform.scale(self.light_surface, (128, 128))
        self.intensity = 500

    def update(self, player):
        self.light_position = player.rect.center

    def draw(self, surface):
        surface.blit(self.ResizeLight, (400, 300), special_flags=pygame.BLEND_RGBA_ADD)