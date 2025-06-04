import pygame

class Player:
    def __init__(self, tilemap):
        self.position = pygame.Vector2(400, 300)
        self.spritesheet = pygame.image.load('../Assets/Arthur.png').convert_alpha()
        self.animations = {
            'down': [self.spritesheet.subsurface((0, 0, 64, 64)), self.spritesheet.subsurface((64, 0, 64, 64))],
            'up': [self.spritesheet.subsurface((0, 64, 64, 64)), self.spritesheet.subsurface((64, 64, 64, 64))],
            'left': [self.spritesheet.subsurface((0, 128, 64, 64)), self.spritesheet.subsurface((64, 128, 64, 64))],
            'right': [self.spritesheet.subsurface((0, 192, 64, 64)), self.spritesheet.subsurface((64, 192, 64, 64))],
        }
        self.current_animation = 'down'
        self.frame_index = 0
        self.image = self.animations[self.current_animation][self.frame_index]
        self.rect = pygame.Rect(self.position.x, self.position.y, 64, 64)
        self.speed = 5
        self.tilemap = tilemap

    def update(self):
        keys = pygame.key.get_pressed()
        new_position = self.position.copy()
        if keys[pygame.K_w]:
            self.rect.y -= self.speed
            self.current_animation = 'up'
        elif keys[pygame.K_s]:
            self.rect.y += self.speed
            self.current_animation = 'down'
        elif keys[pygame.K_a]:
            self.rect.x -= self.speed
            self.current_animation = 'left'
        elif keys[pygame.K_d]:
            self.rect.x += self.speed
            self.current_animation = 'right'
        self.image = self.animations[self.current_animation][self.frame_index]
        self.frame_index = (self.frame_index + 1) % len(self.animations[self.current_animation])
        self.rect.topleft = (new_position.x, new_position.y)
        if not self.tilemap.check_collision(self.rect):
            self.position = new_position
        else:
            self.rect.topleft = (self.position.x, self.position.y)

    def draw(self, surface, camera):
        surface.blit(self.image, camera.apply(self.rect), special_flags=pygame.BLEND_RGBA_ADD)