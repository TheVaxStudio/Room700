import pygame
from Settings import settings as stg

class Player:
    def __init__(self, tilemap):
        self.position = pygame.Vector2(400, 300)
        self.spritesheet = pygame.image.load('../Assets/Arthur.png').convert_alpha()
        self.animations = {
            'up': [
                self.spritesheet.subsurface((0, 192, 64, 64)), 
                self.spritesheet.subsurface((64, 192, 64, 64)),
                self.spritesheet.subsurface((128, 192, 64, 64)),
                self.spritesheet.subsurface((192, 192, 64, 64))
            ],     
            'down': [
                self.spritesheet.subsurface((0, 0, 64, 64)), 
                self.spritesheet.subsurface((64, 0, 64, 64)),
                self.spritesheet.subsurface((128, 0, 64, 64)),
                self.spritesheet.subsurface((192, 0, 64, 64))
            ],
            'left': [
                self.spritesheet.subsurface((0, 64, 64, 64)), 
                self.spritesheet.subsurface((64, 64, 64, 64)),
                self.spritesheet.subsurface((128, 64, 64, 64)),
                self.spritesheet.subsurface((192, 64, 64, 64))
            ],
            'right': [
                self.spritesheet.subsurface((0, 128, 64, 64)), 
                self.spritesheet.subsurface((64, 128, 64, 64)),
                self.spritesheet.subsurface((128, 128, 64, 64)),
                self.spritesheet.subsurface((192, 128, 64, 64))
            ],
            
        }
        self.current_animation = 'down'
        self.frame_index = 0
        self.image = self.animations[self.current_animation][self.frame_index]
        self.rect = pygame.Rect(self.position.x, self.position.y, 64, 64)
        self.speed = stg['player_speed']
        self.tilemap = tilemap

    def update(self, elapsed_frames):
        self.is_standing = False
        keys = pygame.key.get_pressed()
        old_position = self.position.copy()
        x_movement = 0.0
        y_movement = 0.0
        if keys[pygame.K_w]:
            y_movement -= self.speed
            self.current_animation = 'up'
        elif keys[pygame.K_s]:
            y_movement += self.speed
            self.current_animation = 'down'
        elif keys[pygame.K_a]:
            x_movement -= self.speed
            self.current_animation = 'left'
        elif keys[pygame.K_d]:
            x_movement += self.speed
            self.current_animation = 'right'
        else:
            self.is_standing = True
            
        self.image = self.animations[self.current_animation][self.frame_index]
        self.animation_duration_in_frames = stg['animation_duration_in_frames']

        if self.is_standing:
            self.frame_index = 0
        else:
            self.number_of_actual_animations = len(self.animations[self.current_animation])
            self.total_of_animated_frames = self.animation_duration_in_frames * self.number_of_actual_animations
            self.actual_frame_count_of_animations = elapsed_frames % self.total_of_animated_frames
            self.frame_index = int(self.actual_frame_count_of_animations / self.animation_duration_in_frames)

        supposed_rect = pygame.Rect(self.position.x + x_movement, self.position.y + y_movement, self.rect.width, self.rect.height)
        has_player_collided = self.tilemap.check_collision(supposed_rect)
        if has_player_collided:
            self.rect.topleft = old_position
        else:
            self.position.update(self.position.x + x_movement, self.position.y + y_movement)
            self.rect.topleft = (self.position.x, self.position.y)

    def draw(self, surface, camera):
        surface.blit(self.image, camera.apply(self.rect), special_flags=pygame.BLEND_RGBA_ADD)